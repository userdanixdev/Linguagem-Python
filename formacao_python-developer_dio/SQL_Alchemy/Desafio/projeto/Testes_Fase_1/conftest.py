import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SQLASession
from src.database import Base

# Adiciona a representação legível ao usuário no objeto 'Session', versão básica:
#def _session_repr(self):
#    return f"<Session dirty={list(self.dirty)} new={list(self.new)} deleted={list(self.deleted)}>"
#SQLASession.__repr__=_session_repr

# Versão robusta:
def _session_repr(self):
    return (
        f"<Session "
        f"bind={self.bind} | "
        f"dirty(modified)={list(self.dirty)} |\n "
        f"new(newly added)={list(self.new)} | \n"
        f"deleted={list(self.deleted)} | \n"
        f"identity_count={len(self.identity_map)} |\n"
        f"objects={list(self.identity_map.values())}\n"
        f">"
    )
SQLASession.__repr__=_session_repr
SQLASession.__str__ = _session_repr

   
# Fixture de sessão (session)

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:", echo = False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    yield s
    s.close()
    #return Session()

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