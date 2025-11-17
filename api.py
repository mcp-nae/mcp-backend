# api.py
from typing import Union
from client import promptLLM
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. Importar el Middleware

app = FastAPI()

# --- Configuración CORS ---
# Lista de orígenes permitidos. Reemplaza con el dominio de tu Front-end.
origins = [
    "http://localhost:5173",
]

# 2. Agregar el Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,                    # Los orígenes definidos arriba
    allow_credentials=True,                   # Permitir cookies y credenciales
    allow_methods=["*"],                      # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],                      # Permitir todos los encabezados
)
# -------------------------

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/chatbot")
async def send_msg(message: str):
    return await promptLLM(message)