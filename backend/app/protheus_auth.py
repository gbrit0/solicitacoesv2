import httpx
import asyncio
import json

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

# Esta classe irá gerenciar o estado dos tokens de forma segura
class ProtheusAuthenticator:
   def __init__(self, protheus_user: str, protheus_pass: str, protheus_api_url: str):
      self.protheus_user = protheus_user
      self.protheus_pass = protheus_pass
      self.auth_url = protheus_api_url
      self.access_token: str | None = None
      self.refresh_token: str | None = None
      self._lock = asyncio.Lock() # Lock para evitar race conditions na renovação

   async def _perform_login(self):
      """Faz login na API Protheus usando username e password padrão e retorna os JWT Tokens do Protheus."""
      print("Realizando login completo no Protheus...")
      
      params = {
         "grant_type": "password"
      }

      headers = {
         "username": self.protheus_user,
         "password": self.protheus_pass
      }
      async with httpx.AsyncClient() as client:
         try:
            response = await client.post(
               f"{self.auth_url}/api/oauth2/v1/token",
               headers=headers,
               params=params
            )

            response.raise_for_status()
            data = response.json()
         except httpx.HTTPStatusError as exc:
            detail = f"Erro na API Protheus: {exc.response.json()}"

            raise HTTPException(
               status_code=exc.response.status_code,
               detail=detail
            )
         except httpx.RequestError:
            raise HTTPException(
               status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
               detail="Login Protheus: Não foi possível conectar ao serviço de autenticação do Protheus."
            )

      self.access_token = data['access_token']
      self.refresh_token = data['refresh_token']
        
   async def _perform_refresh(self):
      """Atualiza o Bearer Token do Protheus com base no Refresh Token recebido no login."""
      print("Renovando o token de acesso...")
      if not self.refresh_token:
         # Se não há refresh token, precisamos de um login completo
         return await self._perform_login()
      
      try:
         async with httpx.AsyncClient() as client:
            params = {
               "grant_type": "refresh_token",
               "refresh_token": self.refresh_token
            }
            response = await client.post(
               f"{self.auth_url}/api/oauth2/v1/token",
               params=params
            )
            response.raise_for_status()
            new_tokens = response.json()
            self.access_token = new_tokens["access_token"]
            self.refresh_token = new_tokens.get("refresh_token", self.refresh_token)

      except httpx.HTTPStatusError:
         # Se o refresh falhar (ex: refresh_token expirado), tenta um login completo
         await self._perform_login()

   async def get_headers(self) -> dict:
      """Retorna os headers de autorização, garantindo que o token seja válido."""
      async with self._lock:
         if not self.access_token:
            await self._perform_login()
      return {"Authorization": f"Bearer {self.access_token}"}

   async def request(self, method: str, url: str, **kwargs):
      """
      Método wrapper para fazer requisições que automaticamente lida com a renovação de token.
      """
      headers = await self.get_headers()
      kwargs["headers"] = {**kwargs.get("headers", {}), **headers}
      
      async with httpx.AsyncClient(timeout=httpx.Timeout(10.0, connect=60.0)) as client:
         response = await client.request(method, url, **kwargs)
         
         if response.status_code == 401:
            print("Requisição falhou com 401. Renovando token e tentando novamente.")
            # Bloqueia para garantir que apenas uma thread renove
            async with self._lock:
               await self._perform_refresh()
            
            # Tenta novamente com o novo token
            new_headers = await self.get_headers()
            kwargs["headers"] = {**kwargs.get("headers", {}), **new_headers}
            response = await client.request(method, url, **kwargs)

         # Lança uma exceção para qualquer erro remanescente
         response.raise_for_status()
         try:
            data = json.loads(response.content.decode("latin1"))
         except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao decodificar JSON: {str(e)}")
         return JSONResponse(content=data)


