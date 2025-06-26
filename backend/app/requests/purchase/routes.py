import httpx
import os

from fastapi import APIRouter, Depends, Query, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated
from dotenv import load_dotenv

from app.schemas import TokenData
from app.jwt import get_current_user
from app.protheus_auth import login_protheus, refresh_protheus_token

load_dotenv(override=True)

purchase_router = APIRouter(prefix='/purchase')

PROTHEUS_API_URL = os.getenv("PROTHEUS_API_URL")

# --- Endpoint Protegido de Exemplo ---
# @app.get("/users/me")
# async def read_users_me(
#     current_user: Annotated[TokenData, Depends(get_current_user)]
# ):
#     """
#     Um endpoint que só pode ser acessado com um token JWT válido gerado pela nossa API.
#     """
#     return {"username": current_user.username, "message": "Bem-vindo ao seu perfil!"}

@purchase_router.get("", summary="Retorna as solicitações de compras")
async def get_purchase_requests(
   current_user: Annotated[TokenData, Depends(get_current_user)],
   codSolicitacao: Annotated[
                     str | None,
                     Query(
                        title="Código da solicitação",
                        description="Código de uma solicitação específica",
                        example="076235")
                  ] = None,
   limit: Annotated[
            int | None,
            Query(
               title="Limite de resultados",
               description="Inteiro que limita a quantidade de resultados obtidos da API.",
               example=10               
            )
         ] = None,
   offset: Annotated[
               int | None,
               Query(
                  title="Offset de resultados",
                  description="Intervalo de busca?"
               )
            ] = None,
   dataIni: Annotated[
               int | None,
               Query(
                  title="Data inicial",
                  description="Data inicial da busca no formato AAAAMMDD",
                  example=20250626)
               ] = None,
   dataFim: Annotated[
               int | None,
               Query(
                  title="Data final",
                  description="Data final da busca no formato AAAAMMDD",
                  example=20250629
               )
               ] = None,
   auth = None,
   retry: int = 0
):
   """
   Obtém as solicitações de acordo com os parâmetros passados.
   """
   try:
      params = {}
      if codSolicitacao is not None:
         params["codsolic"] = str(codSolicitacao).zfill(6)
      if limit is not None:
         params["limit"] = limit
      if offset is not None:
         params["offset"] = offset
      if dataIni is not None:
         params["dataIni"] = dataIni
      if dataFim is not None:
         params["dataFim"] = dataFim

      if not auth:
         auth = await login_protheus()

      bearer_token = auth["access_token"]
      headers = {"Authorization": f"Bearer {bearer_token}"}

      async with httpx.AsyncClient(timeout=httpx.Timeout(10.0, connect=60.0)) as client:
         response = await client.get(
               f"{PROTHEUS_API_URL}/WSRESTSC1/buscarsolicitacao",
               params=params,
               headers=headers
         )
         response.raise_for_status()
         return JSONResponse(content=response.json())

   except httpx.HTTPStatusError as exc:
      if exc.response.status_code == 401 and retry < 3:
         auth = await refresh_protheus_token(refresh_token=auth["refresh_token"])
         return await get_purchase_requests(
            current_user,
            codSolicitacao,
            limit,
            offset,
            dataIni,
            dataFim,
            auth,
            retry + 1
         )
      raise HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="Não foi possível realizar autenticação junto ao Protheus."
      )

   except httpx.ReadTimeout as e:
      return HTTPException(
         status_code=status.HTTP_408_REQUEST_TIMEOUT,
         detail="A aplicação Protheus demorou muito a responder."
      )
         


   # return {"username": current_user.username, "message": "Bem-vindo ao seu perfil!"}

# async def main():
#    load_dotenv(override=True)
#    req = await get_purchase_requests(codSolicitacao='0726125')

# if __name__ == "__main__":
#    import asyncio
#    asyncio.run(main())