SELECT TOP 100
   R_E_C_N_O_ AS sb1_recno,
   TRIM(B1_COD) + ' - ' + TRIM(B1_DESC) as produto
FROM SB1010
WHERE D_E_L_E_T_ <> '*'
   AND B1_MSBLQL = '2'
   AND B1_FILIAL = '01'