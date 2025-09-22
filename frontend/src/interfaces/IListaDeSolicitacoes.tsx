export default interface IListaDeSolicitacoes {
  requester: string;
  requestDate: Date;
  sc1_recno: number;
  sc: string;
  item: string;
  sb1_recno: number;
  product: string;
  quantity: number;
  ctt_recno: number;
  costCenter: string;
  // ctj_recno: number;
  // apportionment: string;
  needDate: Date;
  observations: string;
  status: string;
  delete: string;
 }