import httpx

from fastapi import APIRouter, Depends, Query, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated, List

from app.schemas import TokenData
from app.jwt import get_current_user

from app.requests.purchase.models import PurchaseRequest

purchase_router = APIRouter(prefix='/compras')

@purchase_router.get("", summary="Retorna as solicitações de compras")
async def get_purchase_requests(
   _: Annotated[TokenData, Depends(get_current_user)],
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
               ] = None
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

      
      # # O método request do  autenticador cuida de tudo.
      # from app.main import protheus_auth
      # api_response_data = await protheus_auth.request(
      #    method="GET",
      #    url=f"{protheus_auth.auth_url}/wsrestsc1/buscarsolicitacao",
      #    params=params
      # )
      
      # return api_response_data
      return JSONResponse(content={"message": "Endpoint de solicitações de compra funcionando!"})   
   
   except httpx.HTTPStatusError as e:
      # Erro que persistiu mesmo após a tentativa de renovação
      raise HTTPException(
         status_code=e.response.status_code,
         detail=f"Erro na API do Protheus: {e.response.json()}"
      )
   # except Exception as e:
   #    # Outros erros inesperados
   #    raise HTTPException(
   #       status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
   #       detail=str(e)
   #    )


@purchase_router.post("", summary="Recebe uma solicitação de compra")
async def post_purchase_requests(
    _: Annotated[TokenData, Depends(get_current_user)],
    request_data: PurchaseRequest
):
   
   from app.main import protheus_auth
   try:
      api_response_data = await protheus_auth.request(
         method="POST",
         url=f"{protheus_auth.auth_url}/wrestsc1/novasolicitacao",
         json=request_data
      )

      return 200, api_response_data
   except httpx.HTTPStatusError as e:
      raise HTTPException(
         status_code=e.response.status_code,
         detail=f"Erro na API do Protheus: {e.response.json()}"
      )
   # except Exception as e:
   #    # Outros erros inesperados
   #    raise HTTPException(
   #       status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
   #       detail=str(e)
   #    )
   