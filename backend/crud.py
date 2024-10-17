from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import Petiano_BD
from schemas import PetianoAtualizar, PetianoBase, PetianoCriar
from fastapi import HTTPException


def criar_petiano(petiano: PetianoCriar, db: Session):
    """Cadastra um novo petiano."""

    # Verifica se o CPF já está sendo usado, se estiver mostra uma mensagem de erro:
    cpf_repetido = db.query(Petiano_BD).filter(Petiano_BD.CPF == petiano.CPF).first()
    if cpf_repetido:
        raise HTTPException(status_code=400, detail="Ja existe um petiano com esse CPF.")

    # Verifica se o e-mail já está sendo usado, se estiver mostra uma mensagem de erro:
    email_repetido = db.query(Petiano_BD).filter(Petiano_BD.Email == petiano.Email).first()
    if email_repetido:
        raise HTTPException(status_code=400, detail="Ja existe um petiano com esse email.")
    
    # Adiciona o petiano no banco de dados
    novo_petiano = Petiano_BD(**petiano.model_dump())
    db.add(novo_petiano)
    db.commit()
    db.refresh(novo_petiano)
    return novo_petiano


def obter_petianos(db: Session):
    """Retorna as informações de todos os petiano."""

    # Retorna uma busca por todos os petianos:
    return db.query(Petiano_BD).all()


def obter_petiano(petiano_id, db: Session):
    """Retorna as informações de um petiano."""
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()

    if petiano:
        return petiano
    
    raise HTTPException(status_code=404, detail="Petiano não encontrado")


def atualizar_petiano(petiano_id: int, petiano_atualizado: PetianoAtualizar, db: Session):
    """Atualiza o cadastro de um petiano a partir de seu id."""

    # Faz a busca pelo petiano:
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()

    # Se o petiano existir, temos que verificar o email
    if petiano:
        # Faz a busca pelo email que será atualizado:
        petiano_com_email_repetido = db.query(Petiano_BD).filter(Petiano_BD.Email == petiano_atualizado.Email).first() 
    
        # Verifica se já existe um registro de email com o email novo e se esse registro é o mesmo que está sendo alterado
        if petiano_com_email_repetido and (int(petiano_com_email_repetido.id) != int(petiano_id)):
            raise HTTPException(status_code=409, detail="Já existe petiano com esse e-mail")
        
        # Faz a atualização e retorna o petiano
        petiano.NomeCompleto = petiano_atualizado.NomeCompleto # type: ignore
        petiano.Email = petiano_atualizado.Email # type: ignore
        petiano.Curso = petiano_atualizado.Curso # type: ignore
        db.commit()
        db.refresh(petiano)
        return petiano
    
    raise HTTPException(status_code=404, detail="Petiano não encontrado")


def remover_petiano(petiano_id: int, db: Session):
    """Remove o registro de um petiano."""

    # Faz a busca pelo petiano:
    petiano = db.query(Petiano_BD).filter(Petiano_BD.id == petiano_id).first()

    # Se o petiano existir, deleta o registro e retorna as informações do petiano excluido.
    if petiano:
        db.delete(petiano)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Petiano não encontrado")
