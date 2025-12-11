import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:", echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Isso cria um banco limpo a cada teste.    
# Os testes da fase 1 servem para verificar as dependências, instâncias,
# modelagem de dados, heranças, poliformismo.
