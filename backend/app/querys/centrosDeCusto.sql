SELECT TOP 20
   R_E_C_N_O_ as ctt_recno,
   TRIM(CTT_CUSTO) + ' - ' + TRIM(CTT_DESC01) AS centro_de_custo
FROM CTT010
WHERE D_E_L_E_T_ <> '*'
   AND CTT_BLOQ = '2'
   AND CTT_FILIAL = '0101'
   AND CTT_CLASSE = '2'