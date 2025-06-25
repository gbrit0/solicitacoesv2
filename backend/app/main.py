from fastapi import FastAPI

from app.requests.purchase.routes import purchase_router
from app.requests.warehouse.routes import warehouse_router
from app.login.login import login_router

app = FastAPI()

app.include_router(purchase_router, prefix='/requests')
app.include_router(warehouse_router, prefix='/requests')
app.include_router(login_router, prefix='/login')