from fastapi import Header, HTTPException, Depends
from app.auth.jwt import validar_token_jwt

def autenticar_usuario(authorization: str = Header(...)):
   if not authorization.startswith("Bearer "):
      raise HTTPException(status_code=401, detail="Token inválido")

   token = authorization.split(" ")[1]
   try:
      return validar_token_jwt(token)
   except:
      raise HTTPException(status_code=401, detail="Token expirado ou inválido")
