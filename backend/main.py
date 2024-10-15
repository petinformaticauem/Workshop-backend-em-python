from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import Base
from database import engine, SessaoLocal
from schemas import PetianoCriar
import crud

# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuração do CORS para permitir requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    """Obtém uma sessão de banco de dados para cada requisição."""
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cadastro", response_model= PetianoCriar)
def criar_petiano(petiano: PetianoCriar, db: Session = Depends(get_db)):
    """Rota para cadastrar um petiano"""
    return crud.criar_petiano(db, petiano)
