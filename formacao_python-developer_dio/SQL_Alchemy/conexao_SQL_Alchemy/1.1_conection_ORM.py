# No processo de conexão com o banco devemos criar um banco de dados para persistir com o processo. Assim usamos o 'engine'
# O método construtor '__init__' foi excluído no processo.
# As sessões vão dar preferência ao construtor '__init__' que é opcional.
# As classes criadas deverão se tornar tabelas dentro de um banco, para isso usamos o 'metadata'
# Devemos em seguida, abrir uma sessão para persistência ao banco de dados.
# Atenção aos importa ORM, deverão ser chamados também.


import sqlalchemy #as sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, inspect, create_engine

# O método 'inspector' irá mostrar o schema data_base do banco de dados vigente
# 'create_engine' irá criar um banco de dados.

# Criação da base de dados:

data_base= declarative_base()

# Criação do Banco de Dados com engine real:

engine = create_engine("sqlite://", echo = True)

# O inspetor:

inspector_engine = inspect(engine)
print(inspector_engine.get_table_names())
# Dentro da documentação do SQL Alchemy, tem os métodos de inspeção da instância 'inspect'.

class User(data_base):
    __tablename__ = "user_account" # Nome da tabela
    # Definir coluna, atributos e restrições:
    id = Column(Integer, primary_key=True,autoincrement=True)
    ft_name = Column(String)
    fl_name = Column(String)
    # O correto é nome da propriedade, não o nome da classe na relação.
    addresses=relationship("Address", back_populates= "user", cascade="all, delete-orphan")
    # OPCIONAL: construtor para usar argumentos posicionais
    #def __init__(self,id, ft_name, fl_name):
    #    self.id = id
    #    self.ft_name = ft_name
    #    self.fl_name = fl_name
    def __repr__(self):  # Método especial 'repr' representando a classe USER, ENTIDADE.
        return f"User (id={self.id}, ft_name={self.ft_name}, fl_name:{self.fl_name})"

class Address(data_base):
    __tablename__ = "Address"
    id = Column(Integer, primary_key=True, autoincrement = True)
    email_address = Column (String(40), nullable=False) # Não poderá ter campos nulos
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses" )
    # OPCIONAL: construtor para usar argumentos posicionais
    #def __init__(self,user_id, email_address):
    #    self.user_id = user_id
    #    self.email_address = email_address    
    def __repr__(self): # Método especial 'repr' representando a classe Address, ENTIDADE.
        return f"Address (id={self.id}, e-mail={self.email_address})"


# O ID está saindo 'None' porque não há um banco de dados. Somente tabelas.
# O SQLAlchemy não coloca os IDs, o banco é quem cria o ID autoincrement;
# Logo o id=None é devido ser antes do commit;
# O banco de dados cria o ID e o SQLAlchemy preenche somente depois do commit.
# Somente após o commit, o banco devolve o ID gerado, e aí o SQLAlchemy preenche o atributo.
# Será necessário criar um engine, criar uma Session. Logo, o objeto criado não irá mais aparecer 'None'

# Atenção! Como você não criou Session, o ID fica None, mesmo com autoincrement.

# Criandos as classes criadas como tabelas e seus atributos no banco de dados:
 
data_base.metadata.create_all(engine)

# Abrindo uma sessão para persistir dados no SQLite:

with Session(engine) as session:

     marisa = User(

        ft_name = "Marisa",
        fl_name = "Marisa Martins",
        addresses = [Address(email_address="marisa@gmail.com"),
        ]
    )
     patrick = User(

        ft_name = "Patrick",
        fl_name = "Patrick Maia",
        addresses = [Address(email_address= "patrick@gmail.com")]
    )

     daniel = User(

        ft_name = "Daniel",
        fl_name = "Martins França",
        addresses = [Address(email_address= "daniel@gmail.com")]
     )
    # Para persistir no BD :
     session.add_all([marisa,patrick,daniel])         
     session.commit()
