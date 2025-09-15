import httpx

from fastapi import APIRouter, Depends, Query, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated

from app.schemas import TokenData
from app.jwt import get_current_user

solicitacoes_router = APIRouter()

@solicitacoes_router.get("", summary="Retorna a lista de solicitações")
async def get_rateios_requests(
   _: Annotated[TokenData, Depends(get_current_user)]
):
   """
   Obtém a lista de solicitações disponíveis no sistema.
   """
   try:   
      # from app.main import protheus_auth
      # # O método request do  autenticador cuida de tudo.
      # api_response_data = await protheus_auth.request(
      #    method="GET",
      #    url=f"{protheus_auth.auth_url}/wsrestsc1/buscarrateios"
      # )
      
      # return api_response_data      ]
      
      content = [
   {
      "requestDate": "2025-09-15",
      "requester": None,
      "sc": 78339,
      "items": [
         {
            "recno": 136726,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "S0000078 - SERVICO DE LOCACAO DE VEICULOS",
            "quantity": 1,
            "needDate": "2025-09-15",
            "observations": "Ve\u00edculo locado para Marcos Vin\u00edcius devido problema em turbo da caminonete REY7E52.Valor total: R$ 1.195,91\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-15",
      "requester": None,
      "sc": 78338,
      "items": [
         {
            "recno": 136725,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "E000H351 - TCF-142 CONVERSOR 485 P/ FIBRA",
            "quantity": 2,
            "needDate": "2025-07-29",
            "observations": "Solicitante: Jos\u00e9 Ot\u00e1vioFornecedor: EM-Tech EnergiaValor: R$1092,00 (cada)Pix na NFNF em anexo\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-15",
      "requester": None,
      "sc": 78337,
      "items": [
         {
            "recno": 136723,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "E000H3B1 - FITA ISOLANTE PRETA",
            "quantity": 200,
            "needDate": "2025-09-25",
            "observations": "ATENDER A DEMANDA DA MONTAGEM DAS VIAS DOS CABOS DE 120MM\u0000"
         },
         {
            "recno": 136724,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "E000H3B2 - FITA ISOLANTE VERDE",
            "quantity": 50,
            "needDate": "2025-09-25",
            "observations": "ATENDER A DEMANDA DA MONTAGEM DAS VIAS DOS CABOS DE 120MM\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-15",
      "requester": None,
      "sc": 78336,
      "items": [
         {
            "recno": 136722,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "F0000224 - 264 EJETOR DE TINTA PISTOLA DE PINTURA KMW",
            "quantity": 20,
            "needDate": "2025-09-16",
            "observations": "10 PE\u00c7AS J\u00c1 VAI PARA PRODU\u00c7\u00c3O E AS OUTRAS 10 VAI FICAR NO ESTOQUE.A TROCA DO MATERIAL \u00c9 FEITA AS 10 PE\u00c7AS DE UMA VEZ.\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-15",
      "requester": None,
      "sc": 78335,
      "items": [
         {
            "recno": 136721,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SMV00002 - PE\u00c7AS PARA MANUTEN\u00c7\u00c3O DA FROTA",
            "quantity": 1,
            "needDate": "2025-09-15",
            "observations": "bateria para fh540 PLACA:QVW8J43\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78334,
      "items": [
         {
            "recno": 136719,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SG000018 - MATERIAL PARA INSTALA\u00c7\u00c3O GMG",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "*Solicita\u00e7\u00e3o:* 078334                                         *Solicitante:* S\u00e9rgio Mota / Afonso Vieira*Aplica\u00e7\u00e3o:* JBS Barra do Gar\u00e7a - MT                                                                                *Descri\u00e7\u00e3o:* Curva de INOX*SC pela* BRG Geradores.\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78333,
      "items": [
         {
            "recno": 136716,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "B0030540 - 961089730054-DEFLETOR MWM",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "cota\u00e7\u00e3o de pe\u00e7as MWMFAVOR ENVIAR COTA\u00c7\u00c3O DAS PE\u00c7AS ACIMA.OBS: somente cota\u00e7\u00e3o\u0000"
         },
         {
            "recno": 136717,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "B0030541 - 961089950014 GRADE RADIADOR MWM",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": None
         },
         {
            "recno": 136718,
            "item": 3,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "B0030259 - 7006269C1E HELICE  6.10TCA MWM",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": None
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78332,
      "items": [
         {
            "recno": 136715,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "A0000022 - SERVICO IFOOD VALE ALIMENTACAO",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "Fornecedor: Ifood Beneficios Motivo: Vale Alimenta\u00e7\u00e3o - 09/25Valor: R$ 116.290,00N\u00b0 NF: 1327246 \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78331,
      "items": [
         {
            "recno": 136713,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SG000018 - MATERIAL PARA INSTALA\u00c7\u00c3O GMG",
            "quantity": 1,
            "needDate": "2025-08-29",
            "observations": "MATERIAL CIVIL PARA SALA DE MAQUINAS DA USINA BIOGAS DA JBS MOZARLANDIA.OBS.: MATERIAL DEVER\u00c1 SER COMPRADO EM MOZARL\u00c2NDIA E ENTEGAR NO BIODIGESTOR DA JBS.\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78330,
      "items": [
         {
            "recno": 136714,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "Fornecedor: Ifood Beneficios Motivo: Vale Alimenta\u00e7\u00e3o - 09/05 Valor: R$ 116.290,00 N\u00b0 NF: 1327246\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78329,
      "items": [
         {
            "recno": 136712,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "Fornecedor: Ifood beneficios Motivo: Opera\u00e7\u00e3o Valor: R$ 18.826,67 N\u00b0 NF: 1333722\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78328,
      "items": [
         {
            "recno": 136709,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "S0000005 - SERVICO MANUTENCAO ALTERNADOR",
            "quantity": 1,
            "needDate": "2025-10-08",
            "observations": "Conserto de 3 alternadores 24v + motor de partida modelo scania.Servi\u00e7os realizados em LEM, pela agrogera.01 nf - 45027 - pe\u00e7as01 nf - 7498 - m\u00e3o de obra.\u0000"
         },
         {
            "recno": 136710,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "S0000005 - SERVICO MANUTENCAO ALTERNADOR",
            "quantity": 1,
            "needDate": "2025-10-08",
            "observations": None
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78327,
      "items": [
         {
            "recno": 136711,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "Fornecimento: Ifood Beneficios Motivo: Opera\u00e7\u00e3o Valor: R$ 18.826,67N\u00b0 NF:1333722\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78326,
      "items": [
         {
            "recno": 136708,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "Fornecedor: Ifood Beneficios Motivo: Reembolso Valor: R$ 905,50 N\u00b0 NF: 1333724\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78325,
      "items": [
         {
            "recno": 136706,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "FM030042 - CAMISETA PERSONALIZADA",
            "quantity": 8,
            "needDate": "2025-09-12",
            "observations": "8 CAMISETAS BRANCAS LISAS. 3 GG3 G2 M\u0000"
         },
         {
            "recno": 136707,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Parcialmente Atendida",
            "product": "FM030035 - CAMISA MANGA LONGA GG",
            "quantity": 8,
            "needDate": "2025-09-12",
            "observations": "8 Camisas sociais a cor branca. Ser\u00e3o Bordadas, segue o tamanho por pessoa: Total: 3 M3 - G1 - GG1 - 4Silvio - M Willian - G C\u00e9lio - MJo\u00e3o Bosco - GGSoninha - GWilson - 4Limirio - MJos\u00e9 Ricardo - G\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78324,
      "items": [
         {
            "recno": 136705,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SG000014 - SERVICO EM BLOCO E PE\u00c7AS DE PRECIS\u00c3O",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "Solicitante Vitor LucianoDescri\u00e7\u00e3o: manuten\u00e7\u00e3o do bloco do motor FPT, serialN.F4EG0485H* 6293704* FPT-SL F601.motor FPT, serialN.F4EG0485H* 6293704* FPT-SL F601.ABF Retifica de MotoresCNPJ 35659301/0001-06Av. Can\u00e3a, quadra 99, lote19 Jardim Novo Mundo.Tel:(62)99229-5875 WhatsappEmail: retificaabf.go@gmail.com\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78323,
      "items": [
         {
            "recno": 136704,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "E000H351 - TCF-142 CONVERSOR 485 P/ FIBRA",
            "quantity": 2,
            "needDate": "2025-07-29",
            "observations": "Solicitante: Jos\u00e9 Ot\u00e1vioFornecedor: EM-Tech EnergiaValor: R$1092,00 (cada)Pix na NF NF em anexo\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-12",
      "requester": None,
      "sc": 78322,
      "items": [
         {
            "recno": 136703,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "SG000018 - MATERIAL PARA INSTALA\u00c7\u00c3O GMG",
            "quantity": 1,
            "needDate": "2025-09-12",
            "observations": "Solicita\u00e7\u00e3o Compra: 078322Solicitante: S\u00e9rgio Mota / Afonso Aplica\u00e7\u00e3o: JBS Mozarl\u00e2ndiaDescri\u00e7\u00e3o:  Material para instala\u00e7\u00e3o linha de G\u00e0s - 04 GENS.C.:\u00a0BRG\u00a0Geradores\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78321,
      "items": [
         {
            "recno": 136702,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "analub filtro para empilhadeira sunward\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78320,
      "items": [
         {
            "recno": 136700,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "E000H35R - INVERSOR ONDA SENOIDAL PURA 3000W",
            "quantity": 3,
            "needDate": "2025-09-14",
            "observations": "DEMANDA PARA SUBSTITUI\u00c7\u00c3O DE 03 UNID. NOBREAK APLICADOS EM TRANSFERENCIAS DE MEDIA TENS\u00c3O COM MOTORIZA\u00c7\u00c3O DE DISJUNTORES DE 220VDC NA AGROGERA BA.MODELO:INVERSOR DE ONDA SENOIDAL PURA TENS\u00c3O DE ENTRADA 24 VDC SA\u00cdDA PARA 220 VAC, COM CARGA DE PICO DE 3000W.\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78319,
      "items": [
         {
            "recno": 136699,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "L0005154 - COMBUSTIVEL",
            "quantity": 7000,
            "needDate": "2025-09-29",
            "observations": "Compra de diesel para a Opera\u00e7\u00e3o da Mineradora Maraca.7.000 Litros a R$ 5,53 o Litro sendo um total de R$ 38.710,00.\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78318,
      "items": [
         {
            "recno": 136698,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "Fatura Unidas, referente a Manutern\u00e7\u00e3o do ve\u00edculo placa SYY3E97.Valor: R$ 642,69Vencimento: 26/09/2025\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78317,
      "items": [
         {
            "recno": 136697,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "SMV00002 - PE\u00c7AS PARA MANUTEN\u00c7\u00c3O DA FROTA",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "CAPITAL GUINDASTEPLACA RBX7H74VALVULA DE PRESSAO DA PATOLA VALOR 497,17\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78316,
      "items": [
         {
            "recno": 136696,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SMV00002 - PE\u00c7AS PARA MANUTEN\u00c7\u00c3O DA FROTA",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "MECANICA MM (BAHIA)PLACA PQN8G52PALHETA LIMPADORLAMPADA LANTERNAVALOR 121,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78315,
      "items": [
         {
            "recno": 136693,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000005 - SERVICO DE CONSULTORIA COMERCIAL",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "Bom dia, segue para pagamento nota fiscal referente a consultoria para venda de geradores. Aprovada pelo David. Inserido por L\u00edvia.\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78314,
      "items": [
         {
            "recno": 136692,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SG000018 - MATERIAL PARA INSTALA\u00c7\u00c3O GMG",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "Solicita\u00e7\u00e3o Compra: 078311Solicitante: S\u00e9rgio Mota / Afonso / GildoAplica\u00e7\u00e3o: JBS Mozarl\u00e2ndiaDescri\u00e7\u00e3o:  Material para instala\u00e7\u00e3o - CIVIL S.C.:\u00a0BRG\u00a0Geradores\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78313,
      "items": [
         {
            "recno": 136691,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "D0000540 - TELA ARTISTICA ARAMADA",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "Aplica\u00e7\u00e3o: Produ\u00e7\u00e3o(Estoque incorreto)\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78312,
      "items": [
         {
            "recno": 136687,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 2,
            "needDate": "2025-09-10",
            "observations": "NF 18040ELKA FFLEXABRACADEIRA MSA-8694R$ 50,26\u0000"
         },
         {
            "recno": 136688,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 2,
            "needDate": "2025-09-10",
            "observations": "NF 18040ELKA FFLEXALUMIN ESPIGAO P/ MANGOTE 3R$ 139,51\u0000"
         },
         {
            "recno": 136689,
            "item": 3,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": "1,5",
            "needDate": "2025-09-10",
            "observations": "NF 18040ELKA FFLEXMANG IND KORAX KONT OLEO 300PSI 3R$ 480,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78311,
      "items": [
         {
            "recno": 136686,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "NF 313.734KGCOTOVELO GALV M/F 90 X 3 BSP REMADI 175,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-11",
      "requester": None,
      "sc": 78310,
      "items": [
         {
            "recno": 136690,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "SF000001 - SERVICO DE FRETE",
            "quantity": 1,
            "needDate": "2025-09-11",
            "observations": "Solicita\u00e7\u00e3o Compra: 078310Solicitante: S\u00e9rgio MotaAplica\u00e7\u00e3o: JBS ItuiutabaDescri\u00e7\u00e3o:  FreteS.C.:\u00a0BRG\u00a0Geradores\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78309,
      "items": [
         {
            "recno": 136684,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "NF 56707 AUTO PE\u00c7AS CEBOL\u00c3OANTIFURTO COMB TANQUE VOLVO FH 220,00\u0000"
         },
         {
            "recno": 136685,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "NF 56707 AUTO PE\u00c7AS CEBOL\u00c3OTAMPA TANQUE TRAVA 55,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78308,
      "items": [
         {
            "recno": 136681,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MC000162 - CAIXA DE ACRILICO",
            "quantity": 20,
            "needDate": "2025-09-10",
            "observations": "Solicitante: Jos\u00e9 Ot\u00e1vioFornecedor: Total Acr\u00edlico An\u00e1polis - 62 9 9438-7007\u0000"
         },
         {
            "recno": 136682,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "E000H250 - SWITCH 8P",
            "quantity": 30,
            "needDate": "2025-09-10",
            "observations": None
         },
         {
            "recno": 136683,
            "item": 3,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "E000H37T - MIKROTIK RB 750R2",
            "quantity": 10,
            "needDate": "2025-09-10",
            "observations": None
         },
         {
            "recno": 136694,
            "item": 4,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "SI000004 - CABO DE REDE CAT5E UTP AZUL CAIXA 305MT",
            "quantity": 1525,
            "needDate": "2025-09-11",
            "observations": None
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78307,
      "items": [
         {
            "recno": 136680,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SE000002 - MATERIAL MANUTEN\u00c7\u00c3O DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Solim\u00e1quinas Usinagem Industrial EIRELI 13068-09-251. Confeccionar 05 Cubos para H\u00e9lice do Ventilador Banco de Carga.2. Material Alum\u00ednio \u00d8 110 x 62mm x Furo 1\u201d 1/2. (\u00d8 38,0)3. Custo Unit\u00e1rio ................................. ?R$ 560,004. Custo Total ................................... ? R$ 2.800,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78306,
      "items": [
         {
            "recno": 136674,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licen\u00e7a do Office 365 utilizada pela Brenda - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "recno": 136675,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licen\u00e7a do Office 365 utilizada pelo David - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "recno": 136676,
            "item": 3,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licen\u00e7a do Office 365 utilizadas pela TI (Eudson, Eduardo, Fernando, Jony, Maria, Marlon) - NF E0100XBCPM...Valor total para este setor: ...R$ 3.606,00\u0000"
         },
         {
            "recno": 136677,
            "item": 4,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licen\u00e7a do Office 365 utilizada pela Giuliana - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "recno": 136678,
            "item": 5,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licen\u00e7a do Office 365 utilizada pelo Guilherme - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "recno": 136679,
            "item": 6,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licen\u00e7a do Office 365 utilizada pela Paula e Silvio - NF E0100XBCPM...Valor total para este setor: ...R$ 1.443,19\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78305,
      "items": [
         {
            "recno": 136672,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "S0000115 - SERVI\u00c7O DE CHAVEIRO",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "NF-132VALOR 85,00SERVI\u00c7O DE CHAVEIRO\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78304,
      "items": [
         {
            "recno": 136671,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "B0009CBV - BARRA CHATA ALUMINIO 6 X 3/4\"",
            "quantity": 2,
            "needDate": "2025-09-10",
            "observations": "Projeto Etanol constru\u00e7\u00e3o de coletor\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78302,
      "items": [
         {
            "recno": 136668,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "MECANCA MM (BAHIA)PLACA PRU1B46ALINHAMENTO E BALANCEAMENTOTROCAR OLEO E FILTROSTROCAR PASTILHAS FREIOTROCAR 02 BARRAS AXIAISTROCAR BUCHAS ESTABILIZADORTROCAR BANDEJAS SUPERIORVALOR 950,00\u0000"
         },
         {
            "recno": 136669,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SMV00002 - PE\u00c7AS PARA MANUTEN\u00c7\u00c3O DA FROTA",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "MECANCA MM (BAHIA)PLACA PRU1B46ALINHAMENTO E BALANCEAMENTOTROCAR OLEO E FILTROSTROCAR PASTILHAS FREIOTROCAR 02 BARRAS AXIAISTROCAR BUCHAS ESTABILIZADORTROCAR BANDEJAS SUPERIORVALOR 3050,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78301,
      "items": [
         {
            "recno": 136667,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "jecafalinhamento e balanceamento fh 540placa QVW8J43VALOR 200,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78300,
      "items": [
         {
            "recno": 136666,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000016 - SERVICO INSTALACAO GERADOR",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Solicita\u00e7\u00e3o Compra: 078300Solicitante: S\u00e9rgio MotaAplica\u00e7\u00e3o:  Marfrig Varzea GrandeDescri\u00e7\u00e3o: Instala\u00e7\u00e3o e Opera\u00e7\u00e3o S.C.:\u00a0BRG\u00a0GeradoresDados banc\u00e1rios em anexo a NF\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78299,
      "items": [
         {
            "recno": 136665,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "MECANICA MM (BAHIA)PLACA SCA4B83SERVI\u00c7O DE GUINCHO VALOR 100,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78298,
      "items": [
         {
            "recno": 136664,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "AUTO PE\u00c7AS ANAPOLIS TROCA DO PARA BRISA PLACA SCA4B83\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78297,
      "items": [
         {
            "recno": 136663,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000022 - SERVICO DE SAUDE/EXAMES",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "SC para realiza\u00e7\u00e3o de exame do colaborador Pedro Henrique Marques Coutinho.Valor: R$ 30,00 Local: Goi\u00e2niaPagamento: Pix: 62 998309004 Obs: Exame ainda n\u00e3o foi realizado \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78296,
      "items": [
         {
            "recno": 136662,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood BeneficiosMotivo: Empreita - 09/25 Valor: R$ 918,24 N\u00b0 NF: 1320094\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78295,
      "items": [
         {
            "recno": 136660,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood BeneficiosMotivo: Hora Extra - Pedro H. Coutinho (dias trabalhados)Valor: R$ 1.152,00 N\u00b0 NF: 1320090 \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78294,
      "items": [
         {
            "recno": 136659,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood Benef\u00edcios Motivo: Hora Extra - Bruno Cordeiro e Silva - 09/25Valor: R$ 422,40 N\u00b0 NF: 1320085 \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78293,
      "items": [
         {
            "recno": 136658,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood Benef\u00edcios Motivo: Reembolso 09/25 Valor: R$ 18.115,65 N\u00b0 NF: 1320576 \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78292,
      "items": [
         {
            "recno": 136657,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood Benef\u00edcios Motivo: Reembolso 09/25 Valor: R$ 14.243,58 N\u00b0 NF: 1320573 \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-10",
      "requester": None,
      "sc": 78291,
      "items": [
         {
            "recno": 136655,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o em Processo de Cota\u00e7\u00e3o",
            "product": "MT000031 - SABAO DE AREIA 2KG",
            "quantity": 1,
            "needDate": "2025-09-30",
            "observations": "NF 5924 CFOP 5910 BRINDE DE SAB\u00c3O AREIALINHA 1 NO VALOR DE R$ 142,22LINHA 2 NO VALOR DE R$ 107,36VALOR TOTAL DA NF 249,58\u0000"
         },
         {
            "recno": 136656,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000031 - SABAO DE AREIA 2KG",
            "quantity": 1,
            "needDate": "2025-09-30",
            "observations": "NF 5924 CFOP 5910 BRINDE DE SAB\u00c3O AREIALINHA 1 NO VALOR DE R$ 142,22LINHA 2 NO VALOR DE R$ 107,36VALOR TOTAL DA NF 249,58\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78290,
      "items": [
         {
            "recno": 136653,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Solicita\u00e7\u00e3o de Mesa de Queijos para 40 pessoas, para o anivers\u00e1rio do Sr. Silvio do dia 10. \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78289,
      "items": [
         {
            "recno": 136652,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "MV000036 - DECORA\u00c7\u00c3O TEM\u00c1TICA CORPORATIVA",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "SC de bal\u00f5es tem\u00e1ticos. Conforme foto anexa na cor dourada. 2 Unidades:1 bal\u00e3o escrito \"Feliz anivers\u00e1rio!\" 1 bal\u00e3o escrito \"Parab\u00e9ns Silvio!\" Sugest\u00e3o de Fornecedor: Baloon Art Or\u00e7amento: R$ 465,00 \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78288,
      "items": [
         {
            "recno": 136651,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000025 - SERVICO DE FRETE SOBRE VENDAS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "FRETE ORNELAS, REFERENTE AO FRETE DE RETORNO DA NOTA 38762 - PPX INDUSTRIA E COMERCIO DE ALUMINIO.VALOR: R$12.952,00VENCIMENTO:18/09/2025\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78287,
      "items": [
         {
            "recno": 136649,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Rejeitada",
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "CAFE RANCHEIRONF 2110093VALOR 750,00\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78286,
      "items": [
         {
            "recno": 136650,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000073 - SERVICO DE LOCACAO DE ARTIGOS PARA FESTA",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Loca\u00e7\u00e3o de m\u00f3veis: 1 aparador para os frios1 aparador para os doces e bolo1 aparador para as bebidas4 suqueiras 6 bistros (sem baqueta)40 ta\u00e7as80 garfos de sobremesa80 pratos de sobremesa\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78285,
      "items": [
         {
            "recno": 136648,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "1 Bolo de anivers\u00e1rio, massa branca de leitinho ninho com recheio de ganache de chocolate. 250 docinhos: 30 - brigadeiros tradicionais 30 - beijinhos 30 - mini palha italiana com ninho  30 - nozes30 - pistache 25 - trufas castanha de caju 25 - trufas frutas vermelhas25 - caixetas amora com mirtilo 25 - ninho com morangoFornecedor j\u00e1 ciente: Dlizy Doce 62 986360371\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78284,
      "items": [
         {
            "recno": 136647,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Rejeitada",
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Solicita\u00e7\u00e3o de compra de bebidas para o anivers\u00e1rio do Sr. S\u00edlvio, amanh\u00e3 10/09 \u00e0s 16h. - Refrigentes (6 garrafas de 2lts - Coca Cola e Guaran\u00e1)- Agu\u00e1 com g\u00e1s (5 garrafas de 1,5lts)- Agua (8 litros) - Suco (6 litros - Uva integral) \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78283,
      "items": [
         {
            "recno": 136646,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "C0000212 - ADESIVOS DIVERSOS",
            "quantity": 2,
            "needDate": "2025-09-15",
            "observations": "Adesivo para atendimento contrato MegawattAdesivo n\u00e3o recortado e impresso Dimensional 65cmx45cm (larguraxaltura)\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78282,
      "items": [
         {
            "recno": 136644,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Compra de biscoito, cafe, bala, capuccino da Rancheiro.Reembolso da colaboradora Camila ValadaresOBS: J\u00e1 est\u00e1 pago \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78281,
      "items": [
         {
            "recno": 136645,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "D0000316 - TUBO DE A\u00c7O CARBONO 10\"",
            "quantity": 120,
            "needDate": "2025-09-15",
            "observations": "Atendimento produ\u00e7\u00e3oEstoque furado\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78280,
      "items": [
         {
            "recno": 136638,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000079 - MULTAS E TAXAS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "MULTAS UNIDAS..VALOR: R$ 114,54VENCIMENTO: 24/09/2025\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78279,
      "items": [
         {
            "recno": 136643,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000025 - SERVICO DE FRETE SOBRE VENDAS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Fatura Transportadora Intrega\u00e7\u00e3o, referente ao frete da nota de venda 12620- TOMIO FUKUDA E OUTROS.ValorR$ 5.400,00Vencimento: 24/09/2025\u0000"
         },
         {
            "recno": 136654,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000025 - SERVICO DE FRETE SOBRE VENDAS",
            "quantity": 1,
            "needDate": "2025-09-10",
            "observations": "Fatura Transportadora Intrega\u00e7\u00e3o, referente ao frete da nota de venda 12620- TOMIO FUKUDA E OUTROS.ValorR$ 700,00Vencimento: 24/09/2025\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78278,
      "items": [
         {
            "recno": 136635,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "B0005144 - CUBO DA HELICE BANCO DE CARGA",
            "quantity": 5,
            "needDate": "2025-09-15",
            "observations": "Aplica\u00e7\u00e3o: Banco de cargas\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78277,
      "items": [
         {
            "recno": 136634,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Bloqueada",
            "product": "C0000274 - CONTENTOR IBC",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Tanque de 1000L modelo IBC para ser adicionado a usina Minerva Bag\u00e9, o mesmo sera retirado na loja por um tecnico \u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78276,
      "items": [
         {
            "recno": 136623,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000008 - AGUA SANITARIA",
            "quantity": 25,
            "needDate": "2025-09-22",
            "observations": None
         },
         {
            "recno": 136624,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000015 - CABO PLASTICO P/ RODO/VASSOURA",
            "quantity": 10,
            "needDate": "2025-09-22",
            "observations": None
         },
         {
            "recno": 136625,
            "item": 3,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "E000H2WK - ESPONJA DE ACO BOMBRIL",
            "quantity": 50,
            "needDate": "2025-09-22",
            "observations": None
         },
         {
            "recno": 136626,
            "item": 4,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000039 - PAPEL TOALHA ROLO",
            "quantity": 210,
            "needDate": "2025-09-15",
            "observations": None
         },
         {
            "recno": 136627,
            "item": 5,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000069 - SACO PLASTICO 15X30",
            "quantity": 1000,
            "needDate": "2025-09-15",
            "observations": None
         },
         {
            "recno": 136628,
            "item": 6,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000070 - SACO PLASTICO 25X40",
            "quantity": 1000,
            "needDate": "2025-09-15",
            "observations": None
         },
         {
            "recno": 136629,
            "item": 7,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000044 - VASSOURA DE PALHA",
            "quantity": 8,
            "needDate": "2025-09-22",
            "observations": None
         },
         {
            "recno": 136630,
            "item": 8,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000025 - VASSOURA DE PELO 30CM",
            "quantity": 5,
            "needDate": "2025-09-22",
            "observations": None
         },
         {
            "recno": 136631,
            "item": 9,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000042 - SACO DE LIXO PRETO 300L REFOR\u00c7ADO",
            "quantity": 1000,
            "needDate": "2025-09-15",
            "observations": None
         },
         {
            "recno": 136632,
            "item": 10,
            "status": "Solicita\u00e7\u00e3o Pendente",
            "product": "MT000041 - SACO DE LIXO PRETO 100L REFOR\u00c7ADO",
            "quantity": 1000,
            "needDate": "2025-09-15",
            "observations": None
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78275,
      "items": [
         {
            "recno": 136633,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "S0000025 - SERVICO DE FRETE SOBRE VENDAS",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "FRETE CONTRATADO PARA ENTREGA DA NOTA 12698, CENTRO DE CUSTO COMERCIAL GERADOR.VALOR: 10.583,00VENCIMENTO: 16/09/2025\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-09",
      "requester": None,
      "sc": 78274,
      "items": [
         {
            "recno": 136619,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Rejeitada",
            "product": "S0000024 - SERVICO DE TELECOMUNICACAO/INTERNET",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Pagamento proporcional - linha LauroR$ 65,24...\u0000"
         },
         {
            "recno": 136620,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Rejeitada",
            "product": "S0000024 - SERVICO DE TELECOMUNICACAO/INTERNET",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Pagamento proporcional - Linha DavidR$ 85,56....\u0000"
         },
         {
            "recno": 136621,
            "item": 3,
            "status": "Solicita\u00e7\u00e3o Rejeitada",
            "product": "S0000024 - SERVICO DE TELECOMUNICACAO/INTERNET",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Pagamento proporcional - Linha CleitonR$ 138,30...\u0000"
         },
         {
            "recno": 136622,
            "item": 4,
            "status": "Solicita\u00e7\u00e3o Rejeitada",
            "product": "S0000024 - SERVICO DE TELECOMUNICACAO/INTERNET",
            "quantity": 1,
            "needDate": "2025-09-09",
            "observations": "Pagamento proporcional - Encargos financeirosR$ 6,62...\u0000"
         }
      ]
   },
   {
      "requestDate": "2025-09-08",
      "requester": None,
      "sc": 78273,
      "items": [
         {
            "recno": 136613,
            "item": 1,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "B0030536 - L025CVA-13B1 BICO INJETOR MWM 4.12TCA",
            "quantity": 6,
            "needDate": "2025-09-08",
            "observations": "Garantia bomba Rossi geradores.\u0000"
         },
         {
            "recno": 136614,
            "item": 2,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "B0030535 - 7135-354P-13B2 KIT PLACA FINAL",
            "quantity": 1,
            "needDate": "2025-09-08",
            "observations": None
         },
         {
            "recno": 136615,
            "item": 3,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "B0030534 - 7135-277H-13B2 JG JUNTAS BOMBA INJETORA",
            "quantity": 1,
            "needDate": "2025-09-08",
            "observations": None
         },
         {
            "recno": 136616,
            "item": 4,
            "status": "Solicita\u00e7\u00e3o Totalmente Atendida",
            "product": "B0030533 - 7135-108-13B2 PALHETA",
            "quantity": 1,
            "needDate": "2025-09-08",
            "observations": None
         }
      ]
   }
]


      return JSONResponse(
         content={
            "message": "Endpoint de solicitações funcionando!", 
            "solicitacoes": content
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