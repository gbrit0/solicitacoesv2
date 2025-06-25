import os
from datetime import datetime, timedelta, timezone
from typing import Annotated

import httpx
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(override=True)

# --- Configurações de Segurança e JWT ---
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
GLPI_API_URL = os.getenv("GLPI_API_URL")

# Validação inicial para garantir que as variáveis foram carregadas
if not all([SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, GLPI_API_URL]):
    raise RuntimeError("Variáveis de ambiente essenciais não foram definidas.")

app = FastAPI()

# --- Modelos Pydantic ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

# --- OAuth2 e Dependências ---
# oauth2_scheme aponta para o endpoint que o cliente deve usar para obter o token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    
    # Aqui você poderia buscar o usuário no seu banco de dados, se necessário
    # user = get_user_from_db(username=token_data.username)
    # if user is None:
    #     raise credentials_exception
    
    return token_data

# --- Endpoint de Login ---
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    Recebe username/password, valida na API terceira e retorna um JWT próprio.
    """
    # Passo 1: Fazer a requisição para a API terceira
    async with httpx.AsyncClient() as client:
        try:
            # Atenção: ajuste o payload conforme a necessidade da API terceira
            # Pode ser JSON, form-data, etc.
            response = await client.post(
                GLPI_API_URL,
                json={"username": form_data.username, "password": form_data.password},
                timeout=10.0 # Define um timeout para a requisição externa
            )
            response.raise_for_status() # Lança exceção para status 4xx ou 5xx
        
        except httpx.HTTPStatusError:
            # Se a API terceira retornou 401, 403, etc.
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário ou senha incorretos na plataforma terceira",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except httpx.RequestError:
            # Se houve um erro de rede ao contatar a API terceira
             raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Não foi possível conectar ao serviço de autenticação externo.",
            )

    # Passo 2: Se a autenticação externa foi bem-sucedida, crie o seu próprio token
    if response.status_code == 200:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        # O "subject" do token (sub) será o nome de usuário.
        # Você pode adicionar outros "claims" se desejar.
        access_token = create_access_token(
            data={"sub": form_data.username}, expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}
    
    # Fallback para outros casos inesperados
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Ocorreu um erro inesperado durante a autenticação.",
    )

# --- Endpoint Protegido de Exemplo ---
@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[TokenData, Depends(get_current_user)]
):
    """
    Um endpoint que só pode ser acessado com um token JWT válido gerado pela nossa API.
    """
    return {"username": current_user.username, "message": "Bem-vindo ao seu perfil!"}