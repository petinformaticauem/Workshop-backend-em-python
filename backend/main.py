from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import Base
from database import engine, SessaoLocal
from schemas import PetianoBase, PetianoListar
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

#CREATE:
@app.post("/cadastro", response_model= PetianoBase)
def criar_petiano(petiano: PetianoBase, db: Session = Depends(get_db)):
    """Rota para cadastrar um petiano"""
    return crud.criar_petiano(petiano, db)

#READ:
@app.get("/petiano", response_model= PetianoListar)
def obter_petiano(petiano_id, db: Session = Depends(get_db)):
    """Rota para listar um petiano cadastrado usando o id"""

    petiano_obtido = crud.obter_petiano(petiano_id, db)
    if petiano_obtido:
        return petiano_obtido
    
    if not petiano_obtido:
        raise HTTPException(status_code=404, detail="Petiano não encontrado")

@app.get("/petianos", response_model= list[PetianoListar])
def obter_petianos(db: Session = Depends(get_db)):
    """Rota para listar todos os petianos cadastrados"""
    return crud.obter_petianos(db)

#UPDATE:
@app.put("/petiano", response_model= PetianoListar)
def atualizar_petiano(petiano_id, nome_atualizado, email_atualizado, curso_atualizado, db: Session = Depends(get_db), ):
    """Rota para atualizar o registro de um petiano"""
    
    #Chama a funcao para atualizar os dados do petiano:
    petiano_atualizado = crud.atualizar_petiano(petiano_id, nome_atualizado, email_atualizado, curso_atualizado, db)
    
    #Se o petiano foi atualizado corretamente, ele é retornado:
    if petiano_atualizado:
        return petiano_atualizado
    
    #Se o petiano nao existir, mostra uma mensagem de erro:
    if not petiano_atualizado:
        raise HTTPException(status_code=404, detail="Petiano não encontrado")

#DELETE
@app.delete("/petianos", response_model= PetianoListar)
def remover_petiano(petiano_id, db: Session = Depends(get_db)):
    """Remove um petiano cadastrado e retorna suas informações"""

    #Chama a função para remover o registro do petiano do BD
    petino_removido = crud.remover_petiano(petiano_id, db) 
    
    # Se o petiano foi removido do BD corretamente, o registro dele é retornado:
    if(petino_removido):
        return petino_removido
    
    # Se o petiano não existir, mostra uma mensagem de erro
    if not petino_removido:
        raise HTTPException(status_code=404, detail="Petiano não encontrado")
