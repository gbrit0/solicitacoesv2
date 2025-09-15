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
            "ctt_recno": 675,
            "centro_de_custo": "19010001 - CONSELHO ADMINISTRATIVO"
         },
         {
            "ctt_recno": 677,
            "centro_de_custo": "20010001 - DIRETORIA ADM FINANCEIRA"
         },
         {
            "ctt_recno": 678,
            "centro_de_custo": "20010002 - CONTROLADORIA"
         },
         {
            "ctt_recno": 679,
            "centro_de_custo": "20010003 - FINANCEIRO/FATURAMENTO LOCAÇÃO"
         },
         {
            "ctt_recno": 680,
            "centro_de_custo": "20010004 - FINANCEIRO/FATURAMENTO INDUSTRIA"
         },
         {
            "ctt_recno": 681,
            "centro_de_custo": "20010005 - CONTABILIDADE/FISCAL"
         },
         {
            "ctt_recno": 682,
            "centro_de_custo": "20010006 - TECNOLOGIA DA INFORMAÇÃO"
         },
         {
            "ctt_recno": 683,
            "centro_de_custo": "20010007 - COMPRAS"
         },
         {
            "ctt_recno": 684,
            "centro_de_custo": "20010008 - JURÍDICO"
         },
         {
            "ctt_recno": 685,
            "centro_de_custo": "20010009 - RECURSOS HUMANOS"
         },
         {
            "ctt_recno": 686,
            "centro_de_custo": "20010010 - DEPARTAMENTO PESSOAL"
         },
         {
            "ctt_recno": 687,
            "centro_de_custo": "20010011 - RECEPCAO/PORTARIA"
         },
         {
            "ctt_recno": 688,
            "centro_de_custo": "20010012 - SEGURANÇA E MEDICINA DO TRABALHO"
         },
         {
            "ctt_recno": 689,
            "centro_de_custo": "20010013 - REFEITORIO"
         },
         {
            "ctt_recno": 691,
            "centro_de_custo": "30010001 - COMERCIAL GERADOR"
         },
         {
            "ctt_recno": 692,
            "centro_de_custo": "30010002 - COMERCIAL PEÇAS"
         },
         {
            "ctt_recno": 693,
            "centro_de_custo": "30010003 - MARKETING"
         },
         {
            "ctt_recno": 695,
            "centro_de_custo": "40010001 - DIRETORIA DE PÓS-VENDAS"
         },
         {
            "ctt_recno": 696,
            "centro_de_custo": "40010002 - ASSISTENCIA TÉCNICA"
         },
         {
            "ctt_recno": 697,
            "centro_de_custo": "40010003 - PÓS-VENDAS INSTALAÇÃO"
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