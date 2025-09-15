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

      content = [
         {
            "sb1_recno": 4,
            "produto": "B0004801 - ARRUELA LISA ZB M10"
         },
         {
            "sb1_recno": 7,
            "produto": "B0004803 - COXIM R-073"
         },
         {
            "sb1_recno": 8,
            "produto": "B0004805 - ARRUELA DE PRESSAO M6"
         },
         {
            "sb1_recno": 9,
            "produto": "E0060001 - CABO DE COBRE 750V 70MM VD"
         },
         {
            "sb1_recno": 10,
            "produto": "E0000001 - MALHA EXPANSIVA 20MM"
         },
         {
            "sb1_recno": 11,
            "produto": "B0004807 - JOELHO 90º MACHO/FEMEA 2\""
         },
         {
            "sb1_recno": 12,
            "produto": "B0004809 - PARAF SEXT ZB 1/4\"X2\""
         },
         {
            "sb1_recno": 13,
            "produto": "D0000001 - BARRA CHATA  ALUMINIO"
         },
         {
            "sb1_recno": 14,
            "produto": "B0004811 - ABRACADEIRA 50X72 CRON"
         },
         {
            "sb1_recno": 15,
            "produto": "B0004812 - BUJAO TIPO TAMPAO 1\""
         },
         {
            "sb1_recno": 16,
            "produto": "B0004813 - BUJAO TIPO TAMPAO 2\""
         },
         {
            "sb1_recno": 17,
            "produto": "B0004814 - BUJAO TIPO TAMPAO 2.1/2\""
         },
         {
            "sb1_recno": 18,
            "produto": "B0004815 - BUCHA RED SEXT PARA TEMOSTATO"
         },
         {
            "sb1_recno": 19,
            "produto": "D0000002 - BENGALA SUSP GALV 1/2\"X200MM"
         },
         {
            "sb1_recno": 21,
            "produto": "E0000002 - BATERIA 100A"
         },
         {
            "sb1_recno": 22,
            "produto": "E0060002 - CABO DE COBRE 750V 70MM VM"
         },
         {
            "sb1_recno": 23,
            "produto": "E0060003 - CABO DE COBRE 750V 70MM PR"
         },
         {
            "sb1_recno": 24,
            "produto": "E0000003 - TERMINAL DE COMPRESSAO 70MM"
         },
         {
            "sb1_recno": 25,
            "produto": "E0000004 - TERMINAL POLO BATERIA 70MM²"
         },
         {
            "sb1_recno": 26,
            "produto": "B0004817 - PARAF SEXT FLANG BC M10X30"
         },
         {
            "sb1_recno": 27,
            "produto": "D0000004 - PLACA  ALUMINIO INDENTIF - PA"
         },
         {
            "sb1_recno": 28,
            "produto": "B0004818 - FLEXIVEL 4\" X 200MM INESCAP"
         },
         {
            "sb1_recno": 29,
            "produto": "B0004820 - PORCA  SEXT FLANG M8"
         },
         {
            "sb1_recno": 30,
            "produto": "B0004823 - CURVA 90° ACO CARB SOLDAVEL 4\""
         },
         {
            "sb1_recno": 31,
            "produto": "D0000005 - TUBO ACO CARBONO 4\" 2MM"
         },
         {
            "sb1_recno": 32,
            "produto": "C0000002 - MANTA  FIBRA CERAMICA"
         },
         {
            "sb1_recno": 33,
            "produto": "C0000003 - PAINEL PSI 40KM³ TEC PRETO 25MM"
         },
         {
            "sb1_recno": 34,
            "produto": "C0000004 - PAINEL PSI 40KM³ TEC PRETO 50MM"
         },
         {
            "sb1_recno": 35,
            "produto": "C0000005 - PAINEL PSI 40KM³ VEU PRETO 50MM"
         },
         {
            "sb1_recno": 39,
            "produto": "B0004826 - FLANGE PERFURADA 4\" X160MM"
         },
         {
            "sb1_recno": 41,
            "produto": "E0000005 - LED COM 4 LAMP P/ ILUMINACAO"
         },
         {
            "sb1_recno": 42,
            "produto": "E0000006 - SPIRAL TUBE PRETO 1/4\""
         },
         {
            "sb1_recno": 43,
            "produto": "E0000007 - ABRACADEIRA HELLERMAN T-50"
         },
         {
            "sb1_recno": 45,
            "produto": "E0060005 - CABO DE COBRE 750V 1,0MM² CZ"
         },
         {
            "sb1_recno": 46,
            "produto": "E0060006 - CABO DE COBRE 750V 2,5MM² CZ"
         },
         {
            "sb1_recno": 48,
            "produto": "E0060008 - CABO DE COBRE 750V 4,0MM PR"
         },
         {
            "sb1_recno": 49,
            "produto": "E0060009 - CABO BLINDADO 4X18 AWG"
         },
         {
            "sb1_recno": 50,
            "produto": "E0000013 - TERMINAL OLHAL VM 1,0MM F-6MM"
         },
         {
            "sb1_recno": 51,
            "produto": "E0000014 - TERMINAL DE COMPRESSAO 120MM"
         },
         {
            "sb1_recno": 52,
            "produto": "B0004827 - PARAF SEXT DE LATAO 3/8X1.1/2\""
         },
         {
            "sb1_recno": 53,
            "produto": "B0004829 - ARRUELA DE PRESSAO 3/8\""
         },
         {
            "sb1_recno": 54,
            "produto": "E0030001 - CONTROLADOR AGC 243"
         },
         {
            "sb1_recno": 55,
            "produto": "E0010001 - DISJUNTOR TRIPOLAR 600 A"
         },
         {
            "sb1_recno": 56,
            "produto": "E0000015 - CARREGADOR BAT DEIF12/5"
         },
         {
            "sb1_recno": 57,
            "produto": "E0000017 - 1SVR405650R BASE PARA RELE ABB"
         },
         {
            "sb1_recno": 58,
            "produto": "E0000019 - BORNE SK 2,5 ABB"
         },
         {
            "sb1_recno": 59,
            "produto": "E0000020 - BORNE PT 2.5 QUAT PHO"
         },
         {
            "sb1_recno": 60,
            "produto": "E0000021 - BORNE PT 2.5 TWIN PHO"
         },
         {
            "sb1_recno": 63,
            "produto": "E0000023 - FIXADOR AUTO-ADESIVO NATURAL"
         },
         {
            "sb1_recno": 64,
            "produto": "E0000024 - JUMPER 10-5A"
         },
         {
            "sb1_recno": 65,
            "produto": "E0000025 - MALHA EXPANSIVA  25MM"
         },
         {
            "sb1_recno": 66,
            "produto": "E0060010 - CABO BLINDADO 2X18 AWG"
         },
         {
            "sb1_recno": 68,
            "produto": "E0000028 - TERMINAL TUBOLAR DUPLO 1,0MM"
         },
         {
            "sb1_recno": 69,
            "produto": "E0000029 - TERMINAL TUBOLAR DUPLO 2,5MM"
         },
         {
            "sb1_recno": 70,
            "produto": "E0000030 - TERMINAL OLHAL VM 1,0MM F5/16\""
         },
         {
            "sb1_recno": 71,
            "produto": "E0000033 - ABRACADEIRA HERLLEMAN T-18"
         },
         {
            "sb1_recno": 72,
            "produto": "E0000034 - CANALETA DE PLASTICO 50X50"
         },
         {
            "sb1_recno": 73,
            "produto": "E0000035 - TRILHO DIN 35"
         },
         {
            "sb1_recno": 74,
            "produto": "E0000036 - RESISTOR 150 OHM"
         },
         {
            "sb1_recno": 75,
            "produto": "B0004832 - PARAF SEXT ZB 1/4\"X1\""
         },
         {
            "sb1_recno": 76,
            "produto": "B0004833 - PARAF SEXT ZB 3/8X3/4"
         },
         {
            "sb1_recno": 77,
            "produto": "E0000037 - BORRACHA PALHETA"
         },
         {
            "sb1_recno": 78,
            "produto": "E0000038 - BOTAO EMERG TRAVA  22MM WEG"
         },
         {
            "sb1_recno": 79,
            "produto": "E0000039 - CHAVE LIGA/DESL TIC-TAC"
         },
         {
            "sb1_recno": 80,
            "produto": "E0000040 - PLACA IDENT \"ILUMINACAO\""
         },
         {
            "sb1_recno": 81,
            "produto": "E0000041 - PLACA IDENT \"BOTAO EMERGENCIA\""
         },
         {
            "sb1_recno": 82,
            "produto": "E0000042 - PLACA IDENT \"CONTROLADOR\""
         },
         {
            "sb1_recno": 83,
            "produto": "E0000043 - PLACA IDENT \"DISJUNTOR\""
         },
         {
            "sb1_recno": 88,
            "produto": "B0004834 - LIQUIDO ARREFECIMENTO VOLVO"
         },
         {
            "sb1_recno": 94,
            "produto": "E0000048 - TC 800/5A ABB"
         },
         {
            "sb1_recno": 514,
            "produto": "E0000049 - DIODO SKN 320/04"
         },
         {
            "sb1_recno": 515,
            "produto": "E0000050 - DIODO SKR 320/04"
         },
         {
            "sb1_recno": 517,
            "produto": "E0000052 - LAMINA"
         },
         {
            "sb1_recno": 519,
            "produto": "E0000054 - TERMINAL CONEC FEMEA  AZ 2,5MM"
         },
         {
            "sb1_recno": 524,
            "produto": "S0000001 - LOCACAO DE GRUPO GERADOR"
         },
         {
            "sb1_recno": 545,
            "produto": "B0004837 - BORRACHA ACO. CENT. SF-D/E 275 16UND"
         },
         {
            "sb1_recno": 546,
            "produto": "B0004838 - BORRACHA LONADA"
         },
         {
            "sb1_recno": 552,
            "produto": "F0000007 - TINTA CINZA ALEUTA"
         },
         {
            "sb1_recno": 597,
            "produto": "E0000056 - REGULADOR TENSAO TH4"
         },
         {
            "sb1_recno": 694,
            "produto": "E0000057 - 1SVR405601R4000 RELE 12/8A  ABB"
         },
         {
            "sb1_recno": 705,
            "produto": "E0000058 - CONVERSOR EL FREQ CFW500 WEG"
         },
         {
            "sb1_recno": 706,
            "produto": "E0020003 - DISJUNTOR MOTOR 32/40A WEG"
         },
         {
            "sb1_recno": 712,
            "produto": "E0030002 - CONTROLADOR AGC 4 MAINS"
         },
         {
            "sb1_recno": 723,
            "produto": "E0000061 - BATERIA 150A"
         },
         {
            "sb1_recno": 724,
            "produto": "E0030003 - CONTROLADOR AGC 3 MAINS"
         },
         {
            "sb1_recno": 725,
            "produto": "E0000062 - MODEM ETHERNET CARMEL"
         },
         {
            "sb1_recno": 726,
            "produto": "D0000017 - GONZO C/ABA 1/2"
         },
         {
            "sb1_recno": 727,
            "produto": "D0000018 - CHUMBADORES CBA 5/16 X 2.1/4"
         },
         {
            "sb1_recno": 729,
            "produto": "E0000063 - BATERIA 135A"
         },
         {
            "sb1_recno": 732,
            "produto": "E0000064 - LUMINARIA LED SOBREPOR"
         },
         {
            "sb1_recno": 733,
            "produto": "E0000065 - PLACA IDENT DO PAINEL"
         },
         {
            "sb1_recno": 734,
            "produto": "E0000066 - PLACA SINALIZACAO PAINEL 50X18"
         },
         {
            "sb1_recno": 735,
            "produto": "E0070008 - CABO PP 1,5MM² PR"
         },
         {
            "sb1_recno": 737,
            "produto": "C0000007 - LA VIDRO DUPLA FACE VEU PRETO"
         },
         {
            "sb1_recno": 739,
            "produto": "E0000068 - POSTE BORNE ST 2,5"
         },
         {
            "sb1_recno": 740,
            "produto": "B0004843 - COXIM 1200 ALTECNICA"
         },
         {
            "sb1_recno": 741,
            "produto": "B0004844 - COXIM 500B ALTECNICA"
         },
         {
            "sb1_recno": 742,
            "produto": "E0000070 - TERMINAL TUBOLAR AM 2,5MM"
         },
         {
            "sb1_recno": 743,
            "produto": "E0000073 - TERMINAL OLHAL AZ 2,5MM F5/16\""
         },
         {
            "sb1_recno": 744,
            "produto": "E0000075 - JUMPER 2-8A"
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