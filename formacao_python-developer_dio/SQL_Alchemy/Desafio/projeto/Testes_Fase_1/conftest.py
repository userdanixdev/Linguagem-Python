import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SQLASession
from src.database import Base
from sqlalchemy.engine.base import Connection # Import da classe real
from sqlalchemy.engine.interfaces import Dialect 
# Diferente de Session, o Connection não é exposto como classe pública para monkey patch simples
# mas PODE SIM ter o '__repr__' sobrescrito, porque é uma classe Python normal. Assim podemos captuar
# e representá-lo. Assim também como o 'dialect'.

# Representação rica do 'dialect':

def __dialect_repr__(self):
    return (
        f"<Dialect\n"
        f"  name={self.name}\n"
        f"  driver={self.driver}\n"
        f"  supports_native_boolean={self.supports_native_boolean}\n"
        f"  supports_sane_rowcount={self.supports_sane_rowcount}\n"
        f"  supports_sane_multi_rowcount={self.supports_sane_multi_rowcount}\n"
        f">"
    )

Dialect.__repr__ = __dialect_repr__

from sqlalchemy.sql.compiler import SQLCompiler

def repr_compiler(compiler: SQLCompiler):
    if not isinstance(compiler, SQLCompiler):
        return f"<Invalid compiler object: {type(compiler)}>"
    try:
        sql = compiler.string
    except Exception:
        sql = "<unavailable>"        
    try:
        params = compiler.params
    except Exception:
        params = "<unavailable>"        
    try:
        stmt_type = compiler.statement.__class__.__name__
    except Exception:
        stmt_type = "<unknown>"  
    try:
        dialect = f"{compiler.dialect.name}+{compiler.dialect.driver}"                                                      
    except Exception:
        dialect = "<unknown>"           
    try:
        positional = compiler.positional
    except Exception:
        positional = "<unknown>"                
    return (
        f"{compiler.__class__.__name__} \n"
        f" module = {compiler.__class__.__module__}\n"
        f" dialect = {dialect}\n"
        f" statement_type = {stmt_type}\n"
        f" sql = {sql!r}\n"
        f" params={params}\n"
        f" positional={positional}\n"
    )        
# Representação rica do COMPILER


# Representação rica do self ( connection ):

def repr_connection(self):
    return (f"< \n"
        f"{self.__class__.__name__}|\n"
        f" dialect = {self.dialect.name}|\n"
        f" driver = {self.dialect.driver}|\n"
        f" engine = {self.engine.url} |\n"
        f" in_transaction={self.in_transaction()}\n"
        f">"
    )
Connection.__repr__ = repr_connection # monkey patch

# Adiciona a representação legível ao usuário no objeto 'Session', versão básica:
#def _session_repr(self):
#    return f"<Session dirty={list(self.dirty)} new={list(self.new)} deleted={list(self.deleted)}>"
#SQLASession.__repr__=_session_repr

# Versão robusta:
def __session_repr__(self):
    return (
        f"<Session "
        f"bind={self.bind} | "
        f"dirty(modified)={list(self.dirty)} |\n "
        f"new(newly added)={[f"{obj.__class__.__name__}(id={getattr(obj, 'id', 'N/A')})" for obj in self.new]} | \n"
        f"deleted={list(self.deleted)} | \n"
        f"identity_count={len(self.identity_map)} |\n"
        f"objects={list(self.identity_map.values())}\n"
        f">"
    )
SQLASession.__repr__=__session_repr__

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