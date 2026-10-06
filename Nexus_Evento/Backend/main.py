from fastapi import FastAPI
from app.database import engine, Base
from app import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="NexoEventos API",
    description="Sistema de gestión para el Centro de Convenciones NexoEventos",
    version="1.0.0"
)


@app.get("/", tags=["General"])
def read_root():
    return {
        "message": "Bienvenido a NexoEventos API",
        "docs": "/docs",
        "status": "online"
    }