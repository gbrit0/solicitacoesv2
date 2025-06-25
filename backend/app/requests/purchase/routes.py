from fastapi import APIRouter, Depends
from typing import Annotated


from app.schemas import TokenData
from app.jwt import get_current_user

purchase_router = APIRouter(prefix='/purchase')

# --- Endpoint Protegido de Exemplo ---
# @app.get("/users/me")
# async def read_users_me(
#     current_user: Annotated[TokenData, Depends(get_current_user)]
# ):
#     """
#     Um endpoint que só pode ser acessado com um token JWT válido gerado pela nossa API.
#     """
#     return {"username": current_user.username, "message": "Bem-vindo ao seu perfil!"}

@purchase_router.get("", summary="Retorna as solicitações de compras")
async def get_purchase_requests(
   current_user: Annotated[TokenData, Depends(get_current_user)]
):
   """
   Obtém as solicitações de acordo com os parâmetros passados.
   """
   return {"username": current_user.username, "message": "Bem-vindo ao seu perfil!"}