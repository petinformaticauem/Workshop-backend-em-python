from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from models import Base
from database import engine, SessaoLocal
import schemas, models, crud, auth

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

# Esquema de autenticação OAuth2 com senha
oauth2_esquema = OAuth2PasswordBearer(tokenUrl="/login")

def get_db():
    """Obtém uma sessão de banco de dados para cada requisição."""
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cadastro", response_model=schemas.Tarefa)
def criar_petiano(tarefa: schemas.TarefaBase, db: Session = Depends(get_db)):
    """Rota para cadastrar um petiano"""
    return crud.criar_petiano(db, tarefa, usuario_id=usuario_atual.id)








@app.get("/login", response_model=List[schemas.Tarefa])
def ler_tarefas(token: str = Depends(oauth2_esquema), db: Session = Depends(get_db)):
    """Rota para obter todas as tarefas do usuário autenticado."""
    usuario_atual = auth.obter_usuario_atual(db, token)
    return crud.obter_tarefas(db, usuario_id=usuario_atual.id)

@app.delete("/petiano")
def deletar_tarefa(tarefa_id: int, token: str = Depends(oauth2_esquema), db: Session = Depends(get_db)):
    """Rota para deletar uma tarefa específica."""
    usuario_atual = auth.obter_usuario_atual(db, token)
    tarefa_deletada = crud.deletar_tarefa(db, tarefa_id, usuario_id=usuario_atual.id)
    if tarefa_deletada is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"detail": "Tarefa removida com sucesso"}

@app.delete("/tarefas")
def deletar_todas_tarefas(token: str = Depends(oauth2_esquema), db: Session = Depends(get_db)):
    """Rota para deletar todas as tarefas do usuário."""
    usuario_atual = auth.obter_usuario_atual(db, token)
    crud.deletar_todas_tarefas(db, usuario_id=usuario_atual.id)
    return {"detail": "Todas as tarefas foram removidas"}

@app.put("/tarefas/{tarefa_id}", response_model=schemas.Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa: schemas.TarefaBase, token: str = Depends(oauth2_esquema), db: Session = Depends(get_db)):
    """Rota para atualizar uma tarefa existente."""
    usuario_atual = auth.obter_usuario_atual(db, token)
    tarefa_atualizada = crud.atualizar_tarefa(db, tarefa_id, usuario_id=usuario_atual.id, descricao=tarefa.descricao)
    if tarefa_atualizada is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa_atualizada

@app.post("/register")
def registrar(usuario: schemas.UsuarioCriar, db: Session = Depends(get_db)):
    """Rota para registrar um novo usuário e retornar um token de acesso."""
    if crud.obter_usuario_por_username(db, username=usuario.username):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    senha_hashed = auth.gerar_hash_senha(usuario.senha)
    usuario_criado = crud.criar_usuario(db, usuario, senha_hashed)
    token_acesso = auth.criar_token_acesso(dados={"sub": usuario.username})
    return {"access_token": token_acesso, "token_type": "bearer"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Rota para autenticar o usuário e fornecer um token de acesso."""
    usuario = auth.autenticar_usuario(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    token_acesso = auth.criar_token_acesso(dados={"sub": usuario.username})
    return {"access_token": token_acesso, "token_type": "bearer"}