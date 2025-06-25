import base64
import httpx
import os
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta
from dotenv import load_dotenv

from app.schemas import Token
from app.jwt import create_access_token

load_dotenv(override=True)

GLPI_API_URL = os.getenv("GLPI_API_URL")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

if not all([ACCESS_TOKEN_EXPIRE_MINUTES, GLPI_API_URL]):
   raise RuntimeError("Variáveis de ambiente essenciais não foram definidas.") 

login_router = APIRouter()

@login_router.post("", response_model=Token, summary="Autentica no GLPI e obtém um token JWT local")
async def login_for_access_token(
   form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
   """
   Recebe username/password, valida na API GLPI via HTTP Basic Auth e retorna um JWT próprio.
   """
   
   auth_string = f"{form_data.username}:{form_data.password}"
   auth_bytes = auth_string.encode("utf-8")
   auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

   headers = {
      "Authorization": f"Basic {auth_base64}"
   }

   async with httpx.AsyncClient() as client:
      try:
         # Loga no GLPI
         response = await client.get(
               f"{GLPI_API_URL}/initSession/",
               headers=headers,
               timeout=10.0
         )
         # Lança uma exceção para respostas de erro (4xx ou 5xx)
         response.raise_for_status()
      
      except httpx.HTTPStatusError as exc:
         if exc.response.status_code == 401:
            detail = "Usuário ou senha incorretos na API do GLPI."
         else:
            detail = f"Erro da API do GLPI: {exc.response.text}"
         
         raise HTTPException(
            status_code=exc.response.status_code,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
         )
      except httpx.RequestError:
         raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Não foi possível conectar ao serviço de autenticação do GLPI.",
         )
   
   glpi_session_data = response.json()
   if "session_token" in glpi_session_data:
      # Logout GLPI
      async with httpx.AsyncClient() as client:
         headers = {
            'Session-Token': glpi_session_data['session_token']
         }
         response = await client.get(
               f"{GLPI_API_URL}/killSession/",
               headers=headers,
               timeout=10.0
         )
         # Lança uma exceção para respostas de erro (4xx ou 5xx)
         response.raise_for_status()

      access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
           
      access_token = create_access_token(
         data={
            "sub": form_data.username
         }, 
         expires_delta=access_token_expires
      )
      
      return {"access_token": access_token, "token_type": "bearer"}
         
   # Fallback para o caso de uma resposta 200 OK mas sem o session_token
   raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail="A resposta da API do GLPI foi bem-sucedida, mas não continha um token de sessão.",
   )