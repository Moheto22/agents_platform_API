from fastapi import FastAPI

from infrastructure.database.database_conexion import DatabaseConexion
from app.users.routers.users_router import app as user_router

app = FastAPI(title="Agent-Platform")

app.on_event("startup")
def startup():
    DatabaseConexion.initialize(5,10)

app.on_event("shutdown")
def shutdown():
    DatabaseConexion.closeConnection()

app.include_router(user_router,prefix="/users",tags=["Users"])