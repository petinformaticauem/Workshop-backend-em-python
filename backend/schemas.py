from pydantic import BaseModel

class PetianoCriar(BaseModel):
    """Esquema base para o petiano."""
    NomeCompleto: str
    CPF: str
    Email: str
    Curso: str
