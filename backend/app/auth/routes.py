from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.auth import glpi, jwt

router = APIRouter()

class LoginInput(BaseModel):
   usuario: str
   senha: str

@router.post("/login")
async def login(data: LoginInput):
   session_token = await glpi.autenticar_usuario(data.usuario, data.senha)
   if not session_token:
      raise HTTPException(status_code=401, detail="Usuário inválido")

   token = jwt.criar_token_jwt({"usuario": data.usuario})
   return {"token": token}
