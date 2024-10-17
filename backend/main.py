<<<<<<< Updated upstream
from fastapi import FastAPI, Depends
=======
from fastapi import FastAPI, Depends, HTTPException, status
>>>>>>> Stashed changes
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import Base
from database import engine, SessaoLocal
from schemas import PetianoAtualizar, PetianoBase, PetianoCriar, PetianoLer
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
@app.post("/petiano", response_model=PetianoLer)
def criar_petiano(petiano: PetianoCriar, db: Session = Depends(get_db)):
    """Rota para cadastrar um petiano"""

    return crud.criar_petiano(petiano, db)


# READ:
@app.get("/petiano/{id}", response_model=PetianoLer)
def obter_petiano(id: int, db: Session = Depends(get_db)):
    """Rota para recuperar os dados de um petiano"""
    
    return crud.obter_petiano(id, db)


@app.get("/petiano", response_model=list[PetianoLer])
def obter_petianos(db: Session = Depends(get_db)):
    """Rota para listar todos os petianos cadastrados"""

    return crud.obter_petianos(db)


# UPDATE:
@app.put("/petiano/{id}", response_model=PetianoLer, request_model=PetianoAtualizar)
def atualizar_petiano(
    id: int,
    petiano: PetianoAtualizar,
    db: Session = Depends(get_db),
):
    """Rota para atualizar o registro de um petiano"""

    return crud.atualizar_petiano(id, petiano, db)


# DELETE
@app.delete("/petiano", status_code=status.HTTP_204_NO_CONTENT)
def remover_petiano(petiano_id, db: Session = Depends(get_db)):
    """Remove um petiano cadastrado e retorna suas informações"""

    crud.remover_petiano(petiano_id, db)
