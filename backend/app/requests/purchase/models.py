from pydantic import BaseModel, Field
from datetime import date

class PurchaseItem(BaseModel):
   product: int = Field(
      ..., example=785463, description="Recno do produto"
   )
   quantity: float = Field(
      ..., example=15.6, description="Quantidade do produto"
   )
   needDate: date = Field(
      ..., example="08/10/2025", description="Data de necessidade"
   )
   observations: str | None = Field(
      None, example="Conserto de 3 alternadores...", description="Observações da solicitação"
   )

class PurchaseRequest(BaseModel):
   requester: str = Field(
      None, example="user.login", description="Solicitante da compra"
   )
   sc: str | None = Field(
      ..., example="078333", description="Número da Solicitação de Compra gerada"
   )
   items: list[PurchaseItem] = Field(
      ..., description="Lista de itens da solicitação de compra"
   )