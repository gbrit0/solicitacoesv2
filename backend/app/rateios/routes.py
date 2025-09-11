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
            "cod_rateio": 1,
            "rateio": "000001 - TODOS VEICULOS"
         },
         {
            "cod_rateio": 2,
            "rateio": "000002 - RATEIO CARRETAS"
         },
         {
            "cod_rateio": 3,
            "rateio": "000003 - STRADAS"
         },
         {
            "cod_rateio": 4,
            "rateio": "000004 - CAMINHOES"
         },
         {
            "cod_rateio": 5,
            "rateio": "000005 - ENERGIA ELÉTRICA (AREA 1)"
         },
         {
            "cod_rateio": 6,
            "rateio": "000006 - ENERGIA ELÉTRICA (AREA 2) MATRIZ"
         },
         {
            "cod_rateio": 7,
            "rateio": "000007 - CLOUD"
         },
         {
            "cod_rateio": 8,
            "rateio": "000008 - MEU RH"
         },
         {
            "cod_rateio": 9,
            "rateio": "000009 - ACESSO PROTHEUS"
         },
         {
            "cod_rateio": 10,
            "rateio": "000010 - MANUTENÇÃO DE ATIVOS"
         },
         {
            "cod_rateio": 11,
            "rateio": "000011 - MEDICINA DO TRABALHO"
         },
         {
            "cod_rateio": 12,
            "rateio": "000012 - RENTAL"
         },
         {
            "cod_rateio": 13,
            "rateio": "000013 - TRANSMITE"
         },
         {
            "cod_rateio": 14,
            "rateio": "000014 - CHECKLIST"
         },
         {
            "cod_rateio": 15,
            "rateio": "000015 - BACKOFFICE DE VENDAS"
         },
         {
            "cod_rateio": 16,
            "rateio": "000016 - FEEDZ"
         },
         {
            "cod_rateio": 17,
            "rateio": "000017 - CUSTO/EST/PCP"
         },
         {
            "cod_rateio": 18,
            "rateio": "000018 - FAT/SESMT/DP"
         },
         {
            "cod_rateio": 19,
            "rateio": "000019 - INTERNET ALGAR"
         },
         {
            "cod_rateio": 20,
            "rateio": "000020 - INTERNET VELOMAX"
         },
         {
            "cod_rateio": 21,
            "rateio": "000021 - TELEFONIA FIREWALL ALGAR"
         },
         {
            "cod_rateio": 22,
            "rateio": "000022 - CONTROLE DE ACESSO - PONTO ELETRÔNICO"
         },
         {
            "cod_rateio": 23,
            "rateio": "000023 - CONTROLE DE ACESSO - CATRACAS / CANCELAS"
         },
         {
            "cod_rateio": 24,
            "rateio": "000024 - TELEFONIA - VIVO"
         },
         {
            "cod_rateio": 25,
            "rateio": "000025 - FAT LOCAÇÃO/FAT PAULO"
         },
         {
            "cod_rateio": 26,
            "rateio": "000026 - LOCAÇÃO/MANUTENÇÃO DE ATIVOS"
         },
         {
            "cod_rateio": 27,
            "rateio": "000027 - AGUA/ESGOTO"
         },
         {
            "cod_rateio": 28,
            "rateio": "000028 - AGUA/ESGOTO (AREA 1)"
         },
         {
            "cod_rateio": 32,
            "rateio": "000032 - SERVICO CLARO INTERNET"
         },
         {
            "cod_rateio": 33,
            "rateio": "000033 - LIMPEZA ELITE"
         },
         {
            "cod_rateio": 34,
            "rateio": "000034 - ALIMENTAÇÃO DE COLABORADORES"
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