# TESTES DA FASE 02 :
# Testes de ORM + Relacionamentos + Consultas Avançadas

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from src.database import Base

from models.base import Base
from models.usuario import Usuario
from models.endereco import Endereco
from models.conta import ContaCorrente, ContaPoupanca
from models.Historico_operacoes import Historico_operacoes

#  FIXTURES DO BANCO DE TESTE
@pytest.fixture
def session():
    engine = create_engine ("sqlite:///:memory:", echo = False)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind = engine)
    return SessionLocal()