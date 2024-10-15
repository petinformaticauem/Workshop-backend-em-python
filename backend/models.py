from sqlalchemy import Column, Integer, String
from database import Base

class Petiano_BD(Base):
    """Modelo de petiano para o banco de dados."""
    __tablename__ = "Petianos"

    id = Column(Integer, primary_key=True)
    NomeCompleto = Column(String, unique=True, index=True)
    Email = Column(String, unique=True, index=True)
    CPF = Column(String, unique=True, index=True)
    Curso = Column(String)
