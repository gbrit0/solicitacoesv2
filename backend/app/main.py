import os

from fastapi import FastAPI
from dotenv import load_dotenv

from app.requests.purchase.routes import purchase_router
from app.requests.warehouse.routes import warehouse_router
from app.login.login import login_router
from app.protheus_auth import ProtheusAuthenticator

app = FastAPI()

load_dotenv(override=True)

PROTHEUS_API_URL=os.getenv("PROTHEUS_API_URL")
PROTHEUS_USER=os.getenv("PROTHEUS_USER")
PROTHEUS_PASS=os.getenv("PROTHEUS_PASS")

if not all([PROTHEUS_API_URL, PROTHEUS_USER, PROTHEUS_PASS]):
   raise RuntimeError("Variáveis de ambiente essenciais não foram definidas")

protheus_auth = ProtheusAuthenticator(
   protheus_user=PROTHEUS_USER,
   protheus_pass=PROTHEUS_PASS,
   protheus_api_url=PROTHEUS_API_URL
)

app.include_router(purchase_router, prefix='/requests')
app.include_router(warehouse_router, prefix='/requests')
app.include_router(login_router, prefix='/login')