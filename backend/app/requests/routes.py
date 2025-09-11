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
            "id": "SC 073-0002",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 3,
            "requestDate": "2025-07-01",
            "needDate": "2025-07-04",
            "observations": "ORÇ. N° 52011ASG(CORRETIVA MAQUINA DE SOLDA)RAFAELPOTENCIOMETRO MULTIVOLTAS 5K3590S 10 VOLTAS62,50 187,50\u0000"
         },
         {
            "id": "SC 073-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 4,
            "requestDate": "2025-07-01",
            "needDate": "2025-07-04",
            "observations": "ORÇ. N° 52011ASG(CORRETIVA MAQUINA DE SOLDA)RAFAELPR20-10K - POTENCIOMETRO10KOHMS55,00 220,00\u0000"
         },
         {
            "id": "078317-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SMV00002 - PEÇAS PARA MANUTENÇÃO DA FROTA",
            "quantity": 1,
            "requestDate": "2025-09-11",
            "needDate": "2025-09-11",
            "observations": "CAPITAL GUINDASTEPLACA RBX7H74VALVULA DE PRESSAO DA PATOLA VALOR 497,17\u0000"
         },
         {
            "id": "078316-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SMV00002 - PEÇAS PARA MANUTENÇÃO DA FROTA",
            "quantity": 1,
            "requestDate": "2025-09-11",
            "needDate": "2025-09-11",
            "observations": "MECANICA MM (BAHIA)PLACA PQN8G52PALHETA LIMPADORLAMPADA LANTERNAVALOR 121,00\u0000"
         },
         {
            "id": "078315-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SA000005 - SERVICO DE CONSULTORIA COMERCIAL",
            "quantity": 1,
            "requestDate": "2025-09-11",
            "needDate": "2025-09-11",
            "observations": "Bom dia, segue para pagamento nota fiscal referente a consultoria para venda de geradores. Aprovada pelo David. Inserido por Lívia.\u0000"
         },
         {
            "id": "078314-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SG000018 - MATERIAL PARA INSTALAÇÃO GMG",
            "quantity": 1,
            "requestDate": "2025-09-11",
            "needDate": "2025-09-11",
            "observations": "Solicitação Compra: 078311Solicitante: Sérgio Mota / Afonso / GildoAplicação: JBS MozarlândiaDescrição:  Material para instalação - CIVIL S.C.: BRG Geradores\u0000"
         },
         {
            "id": "078313-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "D0000540 - TELA ARTISTICA ARAMADA",
            "quantity": 1,
            "requestDate": "2025-09-11",
            "needDate": "2025-09-11",
            "observations": "Aplicação: Produção(Estoque incorreto)\u0000"
         },
         {
            "id": "078312-0003",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": "1,5",
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "NF 18040ELKA FFLEXMANG IND KORAX KONT OLEO 300PSI 3R$ 480,00\u0000"
         },
         {
            "id": "078312-0002",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 2,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "NF 18040ELKA FFLEXALUMIN ESPIGAO P/ MANGOTE 3R$ 139,51\u0000"
         },
         {
            "id": "078312-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 2,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "NF 18040ELKA FFLEXABRACADEIRA MSA-8694R$ 50,26\u0000"
         },
         {
            "id": "078311-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "NF 313.734KGCOTOVELO GALV M/F 90 X 3 BSP REMADI 175,00\u0000"
         },
         {
            "id": "078310-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SF000001 - SERVICO DE FRETE",
            "quantity": 1,
            "requestDate": "2025-09-11",
            "needDate": "2025-09-11",
            "observations": "Solicitação Compra: 078310Solicitante: Sérgio MotaAplicação: JBS ItuiutabaDescrição:  FreteS.C.: BRG Geradores\u0000"
         },
         {
            "id": "078309-0002",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "NF 56707 AUTO PEÇAS CEBOLÃOTAMPA TANQUE TRAVA 55,00\u0000"
         },
         {
            "id": "078309-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "NF 56707 AUTO PEÇAS CEBOLÃOANTIFURTO COMB TANQUE VOLVO FH 220,00\u0000"
         },
         {
            "id": "078308-0004",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SI000004 - CABO DE REDE CAT5E UTP AZUL CAIXA 305MT",
            "quantity": 1525,
            "requestDate": "2025-09-11",
            "needDate": "2025-09-11",
            "observations": "None"
         },
         {
            "id": "078308-0003",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "E000H37T - MIKROTIK RB 750R2",
            "quantity": 5,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "None"
         },
         {
            "id": "078308-0002",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "E000H250 - SWITCH 8P",
            "quantity": 15,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "None"
         },
         {
            "id": "078308-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "MC000162 - CAIXA DE ACRILICO",
            "quantity": 20,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Solicitante: José OtávioFornecedor: Total Acrílico Anápolis - 62 9 9438-7007\u0000"
         },
         {
            "id": "078307-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SE000002 - MATERIAL MANUTENÇÃO DE MAQUINAS E EQUIPAMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Solimáquinas Usinagem Industrial EIRELI 13068-09-251. Confeccionar 05 Cubos para Hélice do Ventilador Banco de Carga.2. Material Alumínio Ø 110 x 62mm x Furo 1” 1/2. (Ø 38,0)3. Custo Unitário ................................. ?R$ 560,004. Custo Total ................................... ? R$ 2.800,00\u0000"
         },
         {
            "id": "078306-0006",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licença do Office 365 utilizada pela Paula e Silvio - NF E0100XBCPM...Valor total para este setor: ...R$ 1.443,19\u0000"
         },
         {
            "id": "078306-0005",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licença do Office 365 utilizada pelo Guilherme - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "id": "078306-0004",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licença do Office 365 utilizada pela Giuliana - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "id": "078306-0003",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licença do Office 365 utilizadas pela TI (Eudson, Eduardo, Fernando, Jony, Maria, Marlon) - NF E0100XBCPM...Valor total para este setor: ...R$ 3.606,00\u0000"
         },
         {
            "id": "078306-0002",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licença do Office 365 utilizada pelo David - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "id": "078306-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SI000003 - SERVICO DE FORNECIMENTO DE SOFTWARES/LICENCAS/APLI",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Pagamento referente ao pagamento proporcional da licença do Office 365 utilizada pela Brenda - NF E0100XBCPM...Valor total para este setor: ...R$ 721,20\u0000"
         },
         {
            "id": "078305-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "S0000115 - SERVIÇO DE CHAVEIRO",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "NF-132VALOR 85,00SERVIÇO DE CHAVEIRO\u0000"
         },
         {
            "id": "078304-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "B0009CBV - BARRA CHATA ALUMINIO 6 X 3/4\"",
            "quantity": 2,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Projeto Etanol construção de coletor\u0000"
         },
         {
            "id": "078302-0002",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SMV00002 - PEÇAS PARA MANUTENÇÃO DA FROTA",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "MECANCA MM (BAHIA)PLACA PRU1B46ALINHAMENTO E BALANCEAMENTOTROCAR OLEO E FILTROSTROCAR PASTILHAS FREIOTROCAR 02 BARRAS AXIAISTROCAR BUCHAS ESTABILIZADORTROCAR BANDEJAS SUPERIORVALOR 3050,00\u0000"
         },
         {
            "id": "078302-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "MECANCA MM (BAHIA)PLACA PRU1B46ALINHAMENTO E BALANCEAMENTOTROCAR OLEO E FILTROSTROCAR PASTILHAS FREIOTROCAR 02 BARRAS AXIAISTROCAR BUCHAS ESTABILIZADORTROCAR BANDEJAS SUPERIORVALOR 950,00\u0000"
         },
         {
            "id": "078301-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "jecafalinhamento e balanceamento fh 540placa QVW8J43VALOR 200,00\u0000"
         },
         {
            "id": "078300-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "S0000016 - SERVICO INSTALACAO GERADOR",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Solicitação Compra: 078300Solicitante: Sérgio MotaAplicação:  Marfrig Varzea GrandeDescrição: Instalação e Operação S.C.: BRG GeradoresDados bancários em anexo a NF\u0000"
         },
         {
            "id": "078299-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "MECANICA MM (BAHIA)PLACA SCA4B83SERVIÇO DE GUINCHO VALOR 100,00\u0000"
         },
         {
            "id": "078298-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "SMV00001 - SERVICO DE MANUTENCAO EM VEICULO/FROTA",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "AUTO PEÇAS ANAPOLIS TROCA DO PARA BRISA PLACA SCA4B83\u0000"
         },
         {
            "id": "078297-0001",
            "status": "Solicitação Pendente",
            "requester": None,
            "product": "S0000022 - SERVICO DE SAUDE/EXAMES",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "SC para realização de exame do colaborador Pedro Henrique Marques Coutinho.Valor: R$ 30,00 Local: GoiâniaPagamento: Pix: 62 998309004 Obs: Exame ainda não foi realizado \u0000"
         },
         {
            "id": "078296-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood BeneficiosMotivo: Empreita - 09/25 Valor: R$ 918,24 N° NF: 1320094\u0000"
         },
         {
            "id": "078295-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood BeneficiosMotivo: Hora Extra - Pedro H. Coutinho (dias trabalhados)Valor: R$ 1.152,00 N° NF: 1320090 \u0000"
         },
         {
            "id": "078294-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood Benefícios Motivo: Hora Extra - Bruno Cordeiro e Silva - 09/25Valor: R$ 422,40 N° NF: 1320085 \u0000"
         },
         {
            "id": "078293-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood Benefícios Motivo: Reembolso 09/25 Valor: R$ 18.115,65 N° NF: 1320576 \u0000"
         },
         {
            "id": "078292-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "SA000021 - SERVICO SALDO LIVRE DIVERSOS",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-10",
            "observations": "Fornecedor: Ifood Benefícios Motivo: Reembolso 09/25 Valor: R$ 14.243,58 N° NF: 1320573 \u0000"
         },
         {
            "id": "078291-0002",
            "status": "Solicitação Pendente",
            "requester": None,
            "product": "MT000031 - SABAO DE AREIA 2KG",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-30",
            "observations": "NF 5924 CFOP 5910 BRINDE DE SABÃO AREIALINHA 1 NO VALOR DE R$ 142,22LINHA 2 NO VALOR DE R$ 107,36VALOR TOTAL DA NF 249,58\u0000"
         },
         {
            "id": "078291-0001",
            "status": "Solicitação em Processo de Cotação",
            "requester": None,
            "product": "MT000031 - SABAO DE AREIA 2KG",
            "quantity": 1,
            "requestDate": "2025-09-10",
            "needDate": "2025-09-30",
            "observations": "NF 5924 CFOP 5910 BRINDE DE SABÃO AREIALINHA 1 NO VALOR DE R$ 142,22LINHA 2 NO VALOR DE R$ 107,36VALOR TOTAL DA NF 249,58\u0000"
         },
         {
            "id": "078290-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "Solicitação de Mesa de Queijos para 40 pessoas, para o aniversário do Sr. Silvio do dia 10. \u0000"
         },
         {
            "id": "078289-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "MV000036 - DECORAÇÃO TEMÁTICA CORPORATIVA",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "SC de balões temáticos. Conforme foto anexa na cor dourada. 2 Unidades:1 balão escrito \"Feliz aniversário!\" 1 balão escrito \"Parabéns Silvio!\" Sugestão de Fornecedor: Baloon Art Orçamento: R$ 465,00 \u0000"
         },
         {
            "id": "078288-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "S0000025 - SERVICO DE FRETE SOBRE VENDAS",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "FRETE ORNELAS, REFERENTE AO FRETE DE RETORNO DA NOTA 38762 - PPX INDUSTRIA E COMERCIO DE ALUMINIO.VALOR: R$12.952,00VENCIMENTO:18/09/2025\u0000"
         },
         {
            "id": "078287-0001",
            "status": "Solicitação Rejeitada",
            "requester": None,
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "CAFE RANCHEIRONF 2110093VALOR 750,00\u0000"
         },
         {
            "id": "078286-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "S0000073 - SERVICO DE LOCACAO DE ARTIGOS PARA FESTA",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "Locação de móveis: 1 aparador para os frios1 aparador para os doces e bolo1 aparador para as bebidas4 suqueiras 6 bistros (sem baqueta)40 taças80 garfos de sobremesa80 pratos de sobremesa\u0000"
         },
         {
            "id": "078285-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "1 Bolo de aniversário, massa branca de leitinho ninho com recheio de ganache de chocolate. 250 docinhos: 30 - brigadeiros tradicionais 30 - beijinhos 30 - mini palha italiana com ninho  30 - nozes30 - pistache 25 - trufas castanha de caju 25 - trufas frutas vermelhas25 - caixetas amora com mirtilo 25 - ninho com morangoFornecedor já ciente: Dlizy Doce 62 986360371\u0000"
         },
         {
            "id": "078284-0001",
            "status": "Solicitação Rejeitada",
            "requester": None,
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "Solicitação de compra de bebidas para o aniversário do Sr. Sílvio, amanhã 10/09 às 16h. - Refrigentes (6 garrafas de 2lts - Coca Cola e Guaraná)- Aguá com gás (5 garrafas de 1,5lts)- Agua (8 litros) - Suco (6 litros - Uva integral) \u0000"
         },
         {
            "id": "078283-0001",
            "status": "Solicitação Bloqueada",
            "requester": None,
            "product": "C0000212 - ADESIVOS DIVERSOS",
            "quantity": 2,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-15",
            "observations": "Adesivo para atendimento contrato MegawattAdesivo não recortado e impresso Dimensional 65cmx45cm (larguraxaltura)\u0000"
         },
         {
            "id": "078282-0001",
            "status": "Solicitação Totalmente Atendida",
            "requester": None,
            "product": "A0000013 - ALIMENTOS",
            "quantity": 1,
            "requestDate": "2025-09-09",
            "needDate": "2025-09-09",
            "observations": "Compra de biscoito, cafe, bala, capuccino da Rancheiro.Reembolso da colaboradora Camila ValadaresOBS: Já está pago \u0000"
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