from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from datetime import timedelta, datetime, timezone
import os
from jose import jwt, JWTError
from typing import Annotated
from dotenv import load_dotenv

from app.schemas import TokenData

load_dotenv(override=True)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
GLPI_API_URL = os.getenv("GLPI_API_URL")

# Validação inicial para garantir que as variáveis foram carregadas
if not all([SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, GLPI_API_URL]):
   raise RuntimeError("Variáveis de ambiente essenciais não foram definidas.")

# oauth2_scheme aponta para o endpoint que o cliente deve usar para obter o token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# --- Funções Auxiliares de JWT ---
def create_access_token(data: dict, expires_delta: timedelta | None = None):
   """Cria um novo token JWT."""
   to_encode = data.copy()
   if expires_delta:
      expire = datetime.now(timezone.utc) + expires_delta
   else:
      # Define uma expiração padrão de 15 minutos se não for fornecida
      expire = datetime.now(timezone.utc) + timedelta(minutes=15)
   
   to_encode.update({"exp": expire})
   encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
   return encoded_jwt

# --- Dependência para obter o usuário atual ---
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
   """Decodifica o token para obter o usuário e valida as credenciais."""
   credentials_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Não foi possível validar as credenciais",
      headers={"WWW-Authenticate": "Bearer"},
   )
   try:
      payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
      username: str = payload.get("sub")
      if username is None:
         raise credentials_exception
      token_data = TokenData(username=username)
   except JWTError:
      raise credentials_exception
   
   return token_data