from sqlalchemy.orm import Session
from models import Petiano_BD
from schemas import PetianoBase

def criar_petiano(petiano: PetianoBase, db: Session):
    """Cadastra um novo petiano."""

    #Verifica se o CPF e email ja estão sendo usados
    cpf_repetido =  db.query(Petiano_BD).filter(Petiano_BD.CPF == petiano.CPF).first()
    if cpf_repetido:
        raise ValueError("Ja existe um petiano com esse CPF.")

    email_repetido =  db.query(Petiano_BD).filter(Petiano_BD.Email == petiano.Email).first()
    if email_repetido:
        raise ValueError("Ja existe um petiano com esse e-mail.")

    #Adiciona o petiano no banco de dados
    if not cpf_repetido and not email_repetido:
        novo_petiano = Petiano_BD(**petiano.dict())
        db.add(novo_petiano)
        db.commit()
        db.refresh(novo_petiano)
        return novo_petiano

def obter_petianos(db: Session):
    """Retorna as informações de todos os petiano."""
    return db.query(Petiano_BD).all()

def obter_petiano(petiano_id, db: Session):
    """Retorna as informações de um petiano."""
    return db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()

def atualizar_petiano(petiano_id: int,nome_atualizado, email_atualizado, curso_atualizado, db: Session):             
    """Atualiza o cadastro de um petiano a partir de seu id."""
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()

    if petiano:
        petiano.NomeCompleto = nome_atualizado
        petiano.Email = email_atualizado
        petiano.Curso = curso_atualizado
        db.commit()
        db.refresh(petiano)
        return petiano

'''
def atualizar_nomecompleto_e_curso_petiano(db: Session,  petiano_id: int, NomeCompleto: str|None, Curso: str|None   ):             
    """Atualiza o cadastro de um petiano."""
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id)
    if petiano:
        petiano.NomeCompleto = NomeCompleto
        petiano.Curso = Curso
        db.commit()
        db.refresh(petiano)
    return petiano
'''

def remover_petiano(petiano_id: int, db: Session):
    """Remove o registro de um petiano.
    Se o petiano for removido, as informações dele serão retornadas"""

    #Faz a busca pelo petiano:
    petiano =  db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()    

    # Se o petiano existir, deleta o registro e retorna as informações do petiano excluido.
    if petiano:
        db.delete(petiano)
        db.commit()
        return petiano
    