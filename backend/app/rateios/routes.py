import httpx

from fastapi import APIRouter, Depends, Query, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated

from app.schemas import TokenData
from app.jwt import get_current_user

rateios_router = APIRouter()

@rateios_router.get("", summary="Retorna a lista de rateios")
async def get_rateios_requests(
   _: Annotated[TokenData, Depends(get_current_user)]
):
   """
   Obtém a lista de rateios disponíveis no sistema.
   """
   try:   
      # from app.main import protheus_auth
      # # O método request do  autenticador cuida de tudo.
      # api_response_data = await protheus_auth.request(
      #    method="GET",
      #    url=f"{protheus_auth.auth_url}/wsrestsc1/buscarrateios"
      # )
      
      # return api_response_data

      content = [
         {
            "rateio": 1,
            "descricao": "TODOS VEICULOS"
         },
         {
            "rateio": 2,
            "descricao": "RATEIO CARRETAS"
         },
         {
            "rateio": 3,
            "descricao": "STRADAS"
         },
         {
            "rateio": 4,
            "descricao": "CAMINHOES"
         },
         {
            "rateio": 5,
            "descricao": "ENERGIA ELÉTRICA (AREA 1)"
         },
         {
            "rateio": 6,
            "descricao": "ENERGIA ELÉTRICA (AREA 2) MATRIZ"
         },
         {
            "rateio": 7,
            "descricao": "CLOUD"
         },
         {
            "rateio": 8,
            "descricao": "MEU RH"
         },
         {
            "rateio": 9,
            "descricao": "ACESSO PROTHEUS"
         },
         {
            "rateio": 10,
            "descricao": "MANUTENÇÃO DE ATIVOS"
         },
         {
            "rateio": 11,
            "descricao": "MEDICINA DO TRABALHO"
         },
         {
            "rateio": 12,
            "descricao": "RENTAL"
         },
         {
            "rateio": 13,
            "descricao": "TRANSMITE"
         },
         {
            "rateio": 14,
            "descricao": "CHECKLIST"
         },
         {
            "rateio": 15,
            "descricao": "BACKOFFICE DE VENDAS"
         },
         {
            "rateio": 16,
            "descricao": "FEEDZ"
         },
         {
            "rateio": 17,
            "descricao": "CUSTO/EST/PCP"
         },
         {
            "rateio": 18,
            "descricao": "FAT/SESMT/DP"
         },
         {
            "rateio": 19,
            "descricao": "INTERNET ALGAR"
         },
         {
            "rateio": 20,
            "descricao": "INTERNET VELOMAX"
         },
         {
            "rateio": 21,
            "descricao": "TELEFONIA FIREWALL ALGAR"
         },
         {
            "rateio": 22,
            "descricao": "CONTROLE DE ACESSO - PONTO ELETRÔNICO"
         },
         {
            "rateio": 23,
            "descricao": "CONTROLE DE ACESSO - CATRACAS / CANCELAS"
         },
         {
            "rateio": 24,
            "descricao": "TELEFONIA - VIVO"
         },
         {
            "rateio": 25,
            "descricao": "FAT LOCAÇÃO/FAT PAULO"
         },
         {
            "rateio": 26,
            "descricao": "LOCAÇÃO/MANUTENÇÃO DE ATIVOS"
         },
         {
            "rateio": 27,
            "descricao": "AGUA/ESGOTO"
         },
         {
            "rateio": 28,
            "descricao": "AGUA/ESGOTO (AREA 1)"
         },
         {
            "rateio": 32,
            "descricao": "SERVICO CLARO INTERNET"
         },
         {
            "rateio": 33,
            "descricao": "LIMPEZA ELITE"
         },
         {
            "rateio": 34,
            "descricao": "ALIMENTAÇÃO DE COLABORADORES"
         }
      ]
      
      return JSONResponse(
         content={
            "message": "Endpoint de rateios funcionando!", 
            "rateios": content
         }
      )
   
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