from sqlalchemy.orm import Session
from models import Petiano_BD
from schemas import PetianoCriar

def criar_petiano(db: Session, petiano: PetianoCriar):
    """Cadastra um novo petiano."""
    db.add(petiano)
    db.commit()
    db.refresh(petiano)
    return petiano

def obter_petiano(db: Session, petiano_id: int):
    """Retorna as informações de um petiano."""
    return db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).all()

def atualizar_petiano(db: Session,  petiano: PetianoCriar):             
    """Atualiza o cadastro de um petiano."""
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano.id)
    if petiano:
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
