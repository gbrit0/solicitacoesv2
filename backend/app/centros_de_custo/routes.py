import httpx

from fastapi import APIRouter, Depends, Query, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated

from app.schemas import TokenData
from app.jwt import get_current_user

cc_router = APIRouter()

@cc_router.get("", summary="Retorna a lista de centros de custos")
async def get_cc_requests(
   _: Annotated[TokenData, Depends(get_current_user)]
):
   """
   Obtém a lista de centros de custos disponíveis no sistema.
   """
   try:   
      # from app.main import protheus_auth
      # # O método request do  autenticador cuida de tudo.
      # api_response_data = await protheus_auth.request(
      #    method="GET",
      #    url=f"{protheus_auth.auth_url}/wsrestsc1/buscarccs"
      # )
      
      # return api_response_data

      content = [
         {
            "cod_cc": 19010001,
            "centro_de_custo": "19010001 - CONSELHO ADMINISTRATIVO"
         },
         {
            "cod_cc": 20010001,
            "centro_de_custo": "20010001 - DIRETORIA ADM FINANCEIRA"
         },
         {
            "cod_cc": 20010002,
            "centro_de_custo": "20010002 - CONTROLADORIA"
         },
         {
            "cod_cc": 20010003,
            "centro_de_custo": "20010003 - FINANCEIRO/FATURAMENTO LOCAÇÃO"
         },
         {
            "cod_cc": 20010004,
            "centro_de_custo": "20010004 - FINANCEIRO/FATURAMENTO INDUSTRIA"
         },
         {
            "cod_cc": 20010005,
            "centro_de_custo": "20010005 - CONTABILIDADE/FISCAL"
         },
         {
            "cod_cc": 20010006,
            "centro_de_custo": "20010006 - TECNOLOGIA DA INFORMAÇÃO"
         },
         {
            "cod_cc": 20010007,
            "centro_de_custo": "20010007 - COMPRAS"
         },
         {
            "cod_cc": 20010008,
            "centro_de_custo": "20010008 - JURÍDICO"
         },
         {
            "cod_cc": 20010009,
            "centro_de_custo": "20010009 - RECURSOS HUMANOS"
         },
         {
            "cod_cc": 20010010,
            "centro_de_custo": "20010010 - DEPARTAMENTO PESSOAL"
         },
         {
            "cod_cc": 20010011,
            "centro_de_custo": "20010011 - RECEPCAO/PORTARIA"
         },
         {
            "cod_cc": 20010012,
            "centro_de_custo": "20010012 - SEGURANÇA E MEDICINA DO TRABALHO"
         },
         {
            "cod_cc": 20010013,
            "centro_de_custo": "20010013 - REFEITORIO"
         },
         {
            "cod_cc": 30010001,
            "centro_de_custo": "30010001 - COMERCIAL GERADOR"
         },
         {
            "cod_cc": 30010002,
            "centro_de_custo": "30010002 - COMERCIAL PEÇAS"
         },
         {
            "cod_cc": 30010003,
            "centro_de_custo": "30010003 - MARKETING"
         },
         {
            "cod_cc": 40010001,
            "centro_de_custo": "40010001 - DIRETORIA DE PÓS-VENDAS"
         },
         {
            "cod_cc": 40010002,
            "centro_de_custo": "40010002 - ASSISTENCIA TÉCNICA"
         },
         {
            "cod_cc": 40010003,
            "centro_de_custo": "40010003 - PÓS-VENDAS INSTALAÇÃO"
         },
         {
            "cod_cc": 50010101,
            "centro_de_custo": "50010101 - DIRETORIA OPERACIONAL"
         },
         {
            "cod_cc": 50010102,
            "centro_de_custo": "50010102 - CONTROLE DE QUALIDADE"
         },
         {
            "cod_cc": 50010103,
            "centro_de_custo": "50010103 - PROJETOS"
         },
         {
            "cod_cc": 50010104,
            "centro_de_custo": "50010104 - PCP"
         },
         {
            "cod_cc": 50010105,
            "centro_de_custo": "50010105 - ALMOXARIFADO"
         },
         {
            "cod_cc": 50010106,
            "centro_de_custo": "50010106 - ENGENHARIA CIVIL"
         },
         {
            "cod_cc": 50010107,
            "centro_de_custo": "50010107 - ENERGIA SOLAR"
         },
         {
            "cod_cc": 50010108,
            "centro_de_custo": "50010108 - ADM LOCAÇÃO"
         },
         {
            "cod_cc": 50010109,
            "centro_de_custo": "50010109 - MANUTENÇÃO GERADOR"
         },
         {
            "cod_cc": 50010110,
            "centro_de_custo": "50010110 - LAVA JATO"
         },
         {
            "cod_cc": 50010111,
            "centro_de_custo": "50010111 - LOGISTICA/FROTA"
         },
         {
            "cod_cc": 50010112,
            "centro_de_custo": "50010112 - INSTALAÇÃO/OPERAÇÃO LOCAÇÃO"
         },
         {
            "cod_cc": 50010113,
            "centro_de_custo": "50010113 - ASSISTENCIA LEM"
         },
         {
            "cod_cc": 50020001,
            "centro_de_custo": "50020001 - GERENCIA DE PRODUÇÃO"
         },
         {
            "cod_cc": 50020101,
            "centro_de_custo": "50020101 - ESTAMPARIA"
         },
         {
            "cod_cc": 50020102,
            "centro_de_custo": "50020102 - SERRALHERIA CHAPA FINA"
         },
         {
            "cod_cc": 50020103,
            "centro_de_custo": "50020103 - PINTURA"
         },
         {
            "cod_cc": 50020201,
            "centro_de_custo": "50020201 - SERRALHERIA CHAPA GROSSA"
         },
         {
            "cod_cc": 50020202,
            "centro_de_custo": "50020202 - JATEAMENTO"
         },
         {
            "cod_cc": 50020203,
            "centro_de_custo": "50020203 - FABRICAÇÃO DE CONTAINERS"
         },
         {
            "cod_cc": 50020301,
            "centro_de_custo": "50020301 - MONTAGEM CARENAGEM"
         },
         {
            "cod_cc": 50020302,
            "centro_de_custo": "50020302 - MONTAGEM MECANICA"
         },
         {
            "cod_cc": 50020401,
            "centro_de_custo": "50020401 - FABRICAÇÃO DE PAINÉIS"
         },
         {
            "cod_cc": 50020402,
            "centro_de_custo": "50020402 - INSTALAÇÃO DE PAINÉIS"
         },
         {
            "cod_cc": 50020403,
            "centro_de_custo": "50020403 - STAR-UP ELÉTRICA"
         },
         {
            "cod_cc": 50020501,
            "centro_de_custo": "50020501 - TUBULAÇÃO ESCAPAMENTOS"
         },
         {
            "cod_cc": 50020502,
            "centro_de_custo": "50020502 - MONTAGEM DE CONTAINERS"
         },
         {
            "cod_cc": 50020601,
            "centro_de_custo": "50020601 - PINTURA LÍQUIDA (UNIDADE I)"
         },
         {
            "cod_cc": 50020701,
            "centro_de_custo": "50020701 - MANUTENÇÃO FÁBRICA/FERRAMENTARIA"
         },
         {
            "cod_cc": 90010001,
            "centro_de_custo": "90010001 - ATUALIZA ESTOQUE"
         },
         {
            "cod_cc": 30010004,
            "centro_de_custo": "30010004 - COMERCIAL ENERGIA"
         },
         {
            "cod_cc": 40010004,
            "centro_de_custo": "40010004 - SUPERVISÓRIO"
         },
         {
            "cod_cc": 20010014,
            "centro_de_custo": "20010014 - SERVICOS GERAIS"
         },
         {
            "cod_cc": 50020002,
            "centro_de_custo": "50020002 - CDT (CENTRO DE DESENV. TECNOLÓGICO)"
         },
         {
            "cod_cc": 50020003,
            "centro_de_custo": "50020003 - CONTROLE DE PRODUÇÃO E ADESIVO"
         },
         {
            "cod_cc": 90020001,
            "centro_de_custo": "90020001 - REFORMA UTE DAIA"
         },
         {
            "cod_cc": 90020002,
            "centro_de_custo": "90020002 - REFORMA REFEITORIO"
         },
         {
            "cod_cc": 90020003,
            "centro_de_custo": "90020003 - CONSTRUCAO CENTRO DE CONVIVENCIA"
         },
         {
            "cod_cc": 90020004,
            "centro_de_custo": "90020004 - JBS BARRA DO GARCAS"
         },
         {
            "cod_cc": 90020005,
            "centro_de_custo": "90020005 - JBS MOZARLANDIA"
         },
         {
            "cod_cc": 90010002,
            "centro_de_custo": "90010002 - PRESTACAO DE SERVICO"
         },
         {
            "cod_cc": 19010002,
            "centro_de_custo": "19010002 - SDO"
         },
         {
            "cod_cc": 30010005,
            "centro_de_custo": "30010005 - COMERCIAL LOCACAO"
         },
         {
            "cod_cc": 50010114,
            "centro_de_custo": "50010114 - FROTA AERONAVES"
         },
         {
            "cod_cc": 50010115,
            "centro_de_custo": "50010115 - HANGAR"
         },
         {
            "cod_cc": 20010015,
            "centro_de_custo": "20010015 - INTELIGENCIA ARTIFICIAL"
         },
         {
            "cod_cc": 50010116,
            "centro_de_custo": "50010116 - LABORATORIO AUTO ELETRICA"
         },
         {
            "cod_cc": 90020006,
            "centro_de_custo": "90020006 - REFORMA GALPAO GRID"
         },
         {
            "cod_cc": 90020007,
            "centro_de_custo": "90020007 - AUDITORIO BRG"
         },
         {
            "cod_cc": 90020008,
            "centro_de_custo": "90020008 - PORTICO GALPAO 3"
         },
         {
            "cod_cc": 90020009,
            "centro_de_custo": "90020009 - CONSTRUCAO LINHA DE VIDA AREA 1"
         },
         {
            "cod_cc": 90010003,
            "centro_de_custo": "90010003 - DEPRECIACAO DESPESA"
         },
         {
            "cod_cc": 90010004,
            "centro_de_custo": "90010004 - DEPRECIACAO CUSTO"
         },
         {
            "cod_cc": 50010117,
            "centro_de_custo": "50010117 - ASSISTENCIA PARÁ"
         }
      ]
      
      return JSONResponse(
         content={
            "message": "Endpoint de centros de custo funcionando!", 
            "centrosDeCusto": content
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