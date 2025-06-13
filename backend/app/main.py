from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.protheus.routes import router as protheus_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(protheus_router, prefix="/protheus")
