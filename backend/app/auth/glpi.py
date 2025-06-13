import os
import httpx
import base64

async def autenticar_usuario(usuario: str, senha: str) -> str | None:
   urlGlpi = os.getenv('GLPI_API_URL')
   
   credenciais = f"{usuario}:{senha}".encode("utf-8")  # transforma string em bytes
   token = base64.b64encode(credenciais).decode("utf-8")  # codifica em base64 e volta pra string

   headers = {
      "Content-Type": "application/json",
      "Authorization": f"Basic {token}"
   }

   async with httpx.AsyncClient() as client:
      resp = await client.post(f"{urlGlpi}/initSession/", headers=headers)
      if resp.status_code == 200:
         headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Session-Token: {resp.json().get('session_token')}"
         }
         await client.post(f"{urlGlpi}/killSession/", headers=headers)
         return 200, "Usuário autenticado com sucesso"
   return None