import httpx

from fastapi import APIRouter, Depends, Query, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated

from app.schemas import TokenData
from app.jwt import get_current_user

products_router = APIRouter()

@products_router.get("", summary="Retorna a lista de produtos")
async def get_purchase_requests(
   _: Annotated[TokenData, Depends(get_current_user)],
   codigo: Annotated[
                     str | None,
                     Query(
                        title="Código do produto",
                        description="Código de um produto específico",
                        example="E000547")
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
            ] = None
):
   """
   Obtém as solicitações de acordo com os parâmetros passados.
   """
   try:
      params = {}
      if codigo is not None:
         params["codigo"] = str(codigo)
      if limit is not None:
         params["limit"] = limit
      if offset is not None:
         params["offset"] = offset

      
      # from app.main import protheus_auth
      # # O método request do  autenticador cuida de tudo.
      # api_response_data = await protheus_auth.request(
      #    method="GET",
      #    url=f"{protheus_auth.auth_url}/wsrestsc1/buscarsolicitacao",
      #    params=params
      # )
      
      # return api_response_data

      content = [ # mock de dados retornados pela API
         {
            "codigo": "B0004801",
            "produto": "B0004801 - ARRUELA LISA ZB M10"
         },
         {
            "codigo": "B0004803",
            "produto": "B0004803 - COXIM R-073"
         },
         {
            "codigo": "B0004805",
            "produto": "B0004805 - ARRUELA DE PRESSAO M6"
         },
         {
            "codigo": "E0060001",
            "produto": "E0060001 - CABO DE COBRE 750V 70MM VD"
         },
         {
            "codigo": "E0000001",
            "produto": "E0000001 - MALHA EXPANSIVA 20MM"
         },
         {
            "codigo": "B0004807",
            "produto": "B0004807 - JOELHO 90º MACHO/FEMEA 2\""
         },
         {
            "codigo": "B0004809",
            "produto": "B0004809 - PARAF SEXT ZB 1/4\"X2\""
         },
         {
            "codigo": "D0000001",
            "produto": "D0000001 - BARRA CHATA  ALUMINIO"
         },
         {
            "codigo": "B0004811",
            "produto": "B0004811 - ABRACADEIRA 50X72 CRON"
         },
         {
            "codigo": "B0004812",
            "produto": "B0004812 - BUJAO TIPO TAMPAO 1\""
         },
         {
            "codigo": "B0004813",
            "produto": "B0004813 - BUJAO TIPO TAMPAO 2\""
         },
         {
            "codigo": "B0004814",
            "produto": "B0004814 - BUJAO TIPO TAMPAO 2.1/2\""
         },
         {
            "codigo": "B0004815",
            "produto": "B0004815 - BUCHA RED SEXT PARA TEMOSTATO"
         },
         {
            "codigo": "D0000002",
            "produto": "D0000002 - BENGALA SUSP GALV 1/2\"X200MM"
         },
         {
            "codigo": "E0000002",
            "produto": "E0000002 - BATERIA 100A"
         },
         {
            "codigo": "E0060002",
            "produto": "E0060002 - CABO DE COBRE 750V 70MM VM"
         },
         {
            "codigo": "E0060003",
            "produto": "E0060003 - CABO DE COBRE 750V 70MM PR"
         },
         {
            "codigo": "E0000003",
            "produto": "E0000003 - TERMINAL DE COMPRESSAO 70MM"
         },
         {
            "codigo": "E0000004",
            "produto": "E0000004 - TERMINAL POLO BATERIA 70MM²"
         },
         {
            "codigo": "B0004817",
            "produto": "B0004817 - PARAF SEXT FLANG BC M10X30"
         },
         {
            "codigo": "D0000004",
            "produto": "D0000004 - PLACA  ALUMINIO INDENTIF - PA"
         },
         {
            "codigo": "B0004818",
            "produto": "B0004818 - FLEXIVEL 4\" X 200MM INESCAP"
         },
         {
            "codigo": "B0004820",
            "produto": "B0004820 - PORCA  SEXT FLANG M8"
         },
         {
            "codigo": "B0004823",
            "produto": "B0004823 - CURVA 90° ACO CARB SOLDAVEL 4\""
         },
         {
            "codigo": "D0000005",
            "produto": "D0000005 - TUBO ACO CARBONO 4\" 2MM"
         },
         {
            "codigo": "C0000002",
            "produto": "C0000002 - MANTA  FIBRA CERAMICA"
         },
         {
            "codigo": "C0000003",
            "produto": "C0000003 - PAINEL PSI 40KM³ TEC PRETO 25MM"
         },
         {
            "codigo": "C0000004",
            "produto": "C0000004 - PAINEL PSI 40KM³ TEC PRETO 50MM"
         },
         {
            "codigo": "C0000005",
            "produto": "C0000005 - PAINEL PSI 40KM³ VEU PRETO 50MM"
         },
         {
            "codigo": "B0004826",
            "produto": "B0004826 - FLANGE PERFURADA 4\" X160MM"
         },
         {
            "codigo": "E0000005",
            "produto": "E0000005 - LED COM 4 LAMP P/ ILUMINACAO"
         },
         {
            "codigo": "E0000006",
            "produto": "E0000006 - SPIRAL TUBE PRETO 1/4\""
         },
         {
            "codigo": "E0000007",
            "produto": "E0000007 - ABRACADEIRA HELLERMAN T-50"
         },
         {
            "codigo": "E0060005",
            "produto": "E0060005 - CABO DE COBRE 750V 1,0MM² CZ"
         },
         {
            "codigo": "E0060006",
            "produto": "E0060006 - CABO DE COBRE 750V 2,5MM² CZ"
         },
         {
            "codigo": "E0060008",
            "produto": "E0060008 - CABO DE COBRE 750V 4,0MM PR"
         },
         {
            "codigo": "E0060009",
            "produto": "E0060009 - CABO BLINDADO 4X18 AWG"
         },
         {
            "codigo": "E0000013",
            "produto": "E0000013 - TERMINAL OLHAL VM 1,0MM F-6MM"
         },
         {
            "codigo": "E0000014",
            "produto": "E0000014 - TERMINAL DE COMPRESSAO 120MM"
         },
         {
            "codigo": "B0004827",
            "produto": "B0004827 - PARAF SEXT DE LATAO 3/8X1.1/2\""
         },
         {
            "codigo": "B0004829",
            "produto": "B0004829 - ARRUELA DE PRESSAO 3/8\""
         },
         {
            "codigo": "E0030001",
            "produto": "E0030001 - CONTROLADOR AGC 243"
         },
         {
            "codigo": "E0010001",
            "produto": "E0010001 - DISJUNTOR TRIPOLAR 600 A"
         },
         {
            "codigo": "E0000015",
            "produto": "E0000015 - CARREGADOR BAT DEIF12/5"
         },
         {
            "codigo": "E0000017",
            "produto": "E0000017 - 1SVR405650R BASE PARA RELE ABB"
         },
         {
            "codigo": "E0000019",
            "produto": "E0000019 - BORNE SK 2,5 ABB"
         },
         {
            "codigo": "E0000020",
            "produto": "E0000020 - BORNE PT 2.5 QUAT PHO"
         },
         {
            "codigo": "E0000021",
            "produto": "E0000021 - BORNE PT 2.5 TWIN PHO"
         },
         {
            "codigo": "E0000023",
            "produto": "E0000023 - FIXADOR AUTO-ADESIVO NATURAL"
         },
         {
            "codigo": "E0000024",
            "produto": "E0000024 - JUMPER 10-5A"
         }
      ]
      
      return JSONResponse(
         content={
            "message": "Endpoint de produtos funcionando!", 
            "data": content
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