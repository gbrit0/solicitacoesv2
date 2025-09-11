from fastapi import APIRouter

warehouse_router = APIRouter(prefix='/almoxarifado')

# --- Endpoint Protegido de Exemplo ---
# @app.get("/users/me")
# async def read_users_me(
#     current_user: Annotated[TokenData, Depends(get_current_user)]
# ):
#     """
#     Um endpoint que só pode ser acessado com um token JWT válido gerado pela nossa API.
#     """
#     return {"username": current_user.username, "message": "Bem-vindo ao seu perfil!"}