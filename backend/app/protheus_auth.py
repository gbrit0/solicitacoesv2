import os
import httpx
import asyncio

from dotenv import load_dotenv

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

load_dotenv(override=True)

PROTHEUS_API_URL=os.getenv("PROTHEUS_API_URL")
PROTHEUS_USER=os.getenv("PROTHEUS_USER")
PROTHEUS_PASS=os.getenv("PROTHEUS_PASS")

if not all([PROTHEUS_API_URL, PROTHEUS_USER, PROTHEUS_PASS]):
   raise RuntimeError("Variáveis de ambiente essenciais não foram definidas")

async def login_protheus():
   """
   Faz login na API Protheus usando username e password padrão e retorna os JWT Tokens do Protheus.
   """

   params = {
      "grant_type": "password"
   }

   headers = {
      "username": PROTHEUS_USER,
      "password": PROTHEUS_PASS
   }
   
   async with httpx.AsyncClient() as client:
      try:
         response = await client.post(
            f"{PROTHEUS_API_URL}/api/oauth2/v1/token",
            headers=headers,
            params=params
         )

         response.raise_for_status()
      except httpx.HTTPStatusError as exc:
         detail = f"Erro na API Protheus: {exc.response.text}"

         raise HTTPException(
            status_code=exc.response.status_code,
            detail=detail
         )
      except httpx.RequestError:
         raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Login Protheus: Não foi possível conectar ao serviço de autenticação do Protheus."
         )
   return response.json()

async def refresh_protheus_token(refresh_token: str):
   """
   Atualiza o Bearer Token do Protheus com base no Refresh Token recebido no login.
   """

   params = {
      "grant_type": "refresh_token",
      "refresh_token": refresh_token
   }

   async with httpx.AsyncClient() as client:
      try:
         response = await client.post(
            f"{PROTHEUS_API_URL}/api/oauth2/v1/token",
            params=params
         )

         response.raise_for_status()

      except httpx.HTTPStatusError as exc:
         detail = f"Erro na API Protheus: {exc.response.text}"

         raise HTTPException(
            status_code=exc.response.status_code,
            detail=detail
         )
      except httpx.RequestError:
         raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Refresh Token: Não foi possível conectar ao serviço de autenticação do Protheus."
         )
   return response.json



# async def main():
#    load_dotenv(override=True)
#    auth = await login_protheus()
   # print("Autenticado no protheus. Atualizando o Bearer...")
   # await refresh_protheus_token(refresh_token=auth['refresh_token'])

# if __name__ == "__main__":
#    asyncio.run(main())