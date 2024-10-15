from sqlalchemy.orm import Session
from models import Petiano_BD
from schemas import PetianoCriar

def criar_petiano(db: Session, petiano: PetianoCriar):
    """Cadastra um novo petiano."""

    novo_petiano = Petiano_BD(**petiano.dict())

    db.add(novo_petiano)
    db.commit()
    db.refresh(novo_petiano)
    return novo_petiano

'''
def obter_petiano(db: Session, petiano_id: int):
    """Retorna as informações de um petiano."""
    return db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).all()

def atualizar_email_petiano(db: Session, petiano_id: int, email: str):             
    """Atualiza o cadastro de um petiano."""
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id)
    if petiano:
        petiano.email = email
        db.commit()
        db.refresh(petiano)
    return petiano

def atualizar_nomecompleto_e_curso_petiano(db: Session,  petiano_id: int, NomeCompleto: str|None, Curso: str|None   ):             
    """Atualiza o cadastro de um petiano."""
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id)
    if petiano:
        petiano.NomeCompleto = NomeCompleto
        petiano.Curso = Curso
        db.commit()
        db.refresh(petiano)
    return petiano

def remover_petiano(db: Session, petiano_id: int):
    """Remove o registro de um petiano."""
    petiano =  db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id)
    if petiano:
        db.delete(petiano)
        db.commit()
    return petiano
'''