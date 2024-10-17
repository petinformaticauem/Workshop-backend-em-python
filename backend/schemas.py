from pydantic import BaseModel


class PetianoBase(BaseModel):
    """Esquema base para o petiano."""

    NomeCompleto: str
    CPF: str
    Email: str
    Curso: str


class PetianoListar(BaseModel):
    """Esquema para listar petianos."""

    id: int
    NomeCompleto: str
    CPF: str
    Email: str
    Curso: str

    class Config:
        orm_mode = True  # Permite que o Pydantic converta objetos ORM em JSON


class PetianoAtualizar(BaseModel):
    """Esquema para atualizar um petiano."""

    NomeCompleto: str
    Email: str
    Curso: str



