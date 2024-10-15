from pydantic import BaseModel
from typing import List

class PetianoBase(BaseModel):
    """Esquema base para o petiano."""
    NomeCompleto: str
    CPF: str
    Email: str
    Curso: str
    Senha: str

class PetianoCriar(PetianoBase):
    """Esquema criar o petiano."""
    NomeCompleto: str
    CPF: str
    Email: str
    Curso: str
    Senha: str
