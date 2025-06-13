import os
from jose import jwt
from datetime import datetime, timedelta

SECRET = os.getenv("JWT_SECRET", "supersegredo")

def criar_token_jwt(dados: dict, expira_em=15):
   exp = datetime.now() + timedelta(minutes=expira_em)
   return jwt.encode({**dados, "exp": exp}, SECRET, algorithm="HS256")

def validar_token_jwt(token: str):
   return jwt.decode(token, SECRET, algorithms=["HS256"])
