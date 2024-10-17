from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import Base
from database import engine, SessaoLocal
from schemas import PetianoAtualizar, PetianoBase, PetianoListar
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


# CREATE:
@app.post("/petiano", response_model=PetianoListar)
def criar_petiano(petiano: PetianoBase, db: Session = Depends(get_db)):
    """Rota para cadastrar um petiano"""
    
    return crud.criar_petiano(petiano, db)


# READ:
@app.get("/petiano")
def obter_petiano(petiano_id=None, db: Session = Depends(get_db)):
    """Rota para listar um petiano cadastrado usando o id ou todos os petianos"""

    if petiano_id:
        return crud.obter_petiano(petiano_id, db)
        
    else:
        return crud.obter_petianos(db)


# @app.get("/petianos", response_model=list[PetianoListar])
# def obter_petianos(db: Session = Depends(get_db)):
#     """Rota para listar todos os petianos cadastrados"""
#     return crud.obter_petianos(db)


# UPDATE:
@app.put("/petiano", response_model=PetianoListar)
def atualizar_petiano(
    petiano_id,
    petiano: PetianoAtualizar,
    db: Session = Depends(get_db),
):
    """Rota para atualizar o registro de um petiano"""

    # Chama a funcao para atualizar os dados do petiano:
    return crud.atualizar_petiano(petiano_id, petiano, db)


# DELETE
@app.delete("/petiano", response_model=PetianoListar)
def remover_petiano(petiano_id, db: Session = Depends(get_db)):
    """Remove um petiano cadastrado e retorna suas informações"""

    # Chama a função para remover o registro do petiano do BD
    return crud.remover_petiano(petiano_id, db)