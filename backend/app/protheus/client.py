import os
import httpx

async def buscar_dados_protheus():
   auth = (os.getenv("PROTHEUS_USER"), os.getenv("PROTHEUS_PASS"))
   url = f"{os.getenv('PROTHEUS_API_URL')}/clientes"

   async with httpx.AsyncClient() as client:
      resp = await client.get(url, auth=auth)
      return resp.json()
