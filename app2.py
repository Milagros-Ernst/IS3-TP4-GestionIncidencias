from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, create_engine
from evento2 import Evento
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Crear las tablas en la base de datos
SQLModel.metadata.create_all(engine)


app= FastAPI()
@app.get("/")
def index():
    return {"message":"Hola Mundo!"}