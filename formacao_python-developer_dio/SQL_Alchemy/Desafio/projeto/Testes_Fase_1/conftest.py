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



# A ORDEM É:

# 1. pytest chama a fixture
# 2. a fixture cria um banco limpo
# 3  pytest executa o teste
# 4  o banco é destruído
# 5  No próximo teste a fixture roda novamente

# Isso é exatamente o comportamento desejado.
# Cada teste começa com banco limpo → isso garante isolamento
# Esse é o padrão em testes unitários.

# EXEMPLOS DE TESTES DA FASE 1 (o que você deve testar)

# ✔ Persistência de atributos;
# Criar modelo, salvar no banco, verificar se id foi gerado;

# ✔ Relacionamentos;
# Criar usuário → criar conta → relacionar;

# ✔ Herança polimórfica
# Criar ContaCorrente, ContaPoupanca e ContaInvestimento e verificar que o tipo_conta diferencia os tipos.

# ✔ Métodos das classes:
#  depositar, sacar, transferir, rendimento da poupança, resgate da conta investimento