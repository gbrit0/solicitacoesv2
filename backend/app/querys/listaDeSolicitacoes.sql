SELECT DISTINCT TOP 100
   TRIM(C1_XSOLWEB) as requester,
   TRY_CAST(C1_EMISSAO AS DATE) as requestDate,
   SC1010.R_E_C_N_O_ AS sc1_recno,
   TRIM(C1_NUM) AS sc,
   TRIM(C1_ITEM) as item,
   SB1010.R_E_C_N_O_ AS sb1_recno,
   TRIM(C1_PRODUTO) + ' - ' + TRIM(C1_DESCRI) as product,
   C1_QUANT as quantity,
   CTT010.R_E_C_N_O_ AS ctt_recno,
   TRIM(CTT_DESC01) AS costCenter,
   -- C1_RATEIO AS apportionment,
   TRY_CAST(C1_DATPRF AS DATE) as needDate,
   TRY_CAST(C1_XOBMEMO AS VARCHAR(MAX)) as observations,
   CASE
      WHEN C1_QUJE = 0 AND (C1_COTACAO = '      ' OR C1_COTACAO = 'IMPORT') AND C1_APROV = 'B' THEN 'Solicitação Bloqueada'
      WHEN C1_QUJE = 0 AND C1_COTACAO = '      ' AND C1_APROV = 'L' THEN 'Solicitação Pendente'
      WHEN C1_QUANT = C1_QUJE THEN 'Solicitação Totalmente Atendida'
      WHEN C1_QUJE > 0 AND C1_QUJE < C1_QUANT AND C1_COTACAO = 'XXXXXX' THEN 'Solicitação Parcialmente Atendida Utilizada em Cotação'
      WHEN C1_QUJE > 0 AND C1_QUJE < C1_QUANT THEN 'Solicitação Parcialmente Atendida'
      WHEN C1_COTACAO != '      ' THEN 'Solicitação em Processo de Cotação'
      WHEN C1_RESIDUO = 'S' THEN 'Elim. por Resíduo'
      WHEN C1_IMPORT = 'S' THEN 'Solicitação de Produto Importado'
      WHEN C1_QUJE = 0 AND (C1_COTACAO = '      ' OR C1_COTACAO = 'IMPORT') AND C1_APROV = 'R' THEN 'Solicitação Rejeitada'
      WHEN C1_RESIDUO = 'S' AND C1_COMPRAC = '1' THEN 'Solicitação em Compra Centralizada'
      ELSE 'Status Indefinido'
   END AS status

FROM SC1010
   LEFT JOIN SB1010
   ON B1_COD = C1_PRODUTO
      AND B1_FILIAL = SUBSTRING(C1_FILIAL, 1, 2)

   LEFT JOIN CTT010
   ON CTT010.D_E_L_E_T_ <> '*' 
   AND CTT_FILIAL = C1_FILIAL
   AND CTT_CUSTO = C1_CC

WHERE
   SC1010.D_E_L_E_T_ <> '*' 
   AND C1_FILIAL = '0101'
   AND C1_NUM NOT LIKE '%[A-Z]%'
   -- AND C1_RATEIO = '1'

ORDER BY 2 DESC;
