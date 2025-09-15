import IItemDeCompra from "./IItemDeCompra";

export default interface IListaDeSolicitacoes {
  requestDate: string;
  requester: string;
  sc: string;
  items: [IItemDeCompra]
}