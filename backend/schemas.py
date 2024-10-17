from pydantic import BaseModel


class PetianoBase(BaseModel):
    """Esquema base para o petiano."""

    NomeCompleto: str
    CPF: str
    Email: str
    Curso: str

class PetianoCriar(PetianoBase):
    """Esquema para criar um petiano."""
    pass


class PetianoLer(PetianoBase):
    """Esquema para ler petianos."""

    id: int

    class Config:
        from_attributes = True  # Permite que o Pydantic converta objetos ORM em JSON


class PetianoAtualizar(BaseModel):
    """Esquema para atualizar um petiano."""

    NomeCompleto: str
    Email: str
    Curso: str
