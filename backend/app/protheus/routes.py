from fastapi import APIRouter, Depends, HTTPException
from app.middleware.auth import autenticar_usuario
from app.protheus.client import buscar_dados_protheus

router = APIRouter()

@router.get("/clientes")
async def get_clientes(usuario=Depends(autenticar_usuario)):
   try:
      dados = await buscar_dados_protheus()
      return dados
   except:
      raise HTTPException(status_code=500, detail="Erro ao acessar o Protheus")
