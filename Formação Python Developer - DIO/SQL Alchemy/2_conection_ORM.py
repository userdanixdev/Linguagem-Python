# 2º Conexão com SQL Alchemy via Python.
# A 2º versão será instanciada via argumentos posicionais
# Para isso os parâmetros serão alterados.
# ATENÇÃO! Podemos instanciar um objeto SQLAlchemy usando argumentos posicionais, 
# sem precisar nomear cada atributo feita pela 1º conexão.

# pip install sqlalchemy
import sqlalchemy 
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeiggnKey

data_base = declarative_base()

class User(data_base):
    __tablename__ = "user_account" # Nome da tabela
    # Definir coluna, atributos e restrições:
    id = Column(Integer, primary_key=True,autoincrement=True)
    ft_name = Column(String)
    fl_name = Column(String)
    # O correto é nome da propriedade, não o nome da classe na relação.
    addresses=relationship("Address", back_populates= "user", cascade="all, delete-orphan")
    # OPCIONAL: construtor para usar argumentos posicionais
    def __init__(self,id, ft_name, fl_name):
        self.id = id
        self.ft_name = ft_name
        self.fl_name = fl_name
    def __repr__(self):  # Método especial 'repr' representando a classe USER, ENTIDADE.
        return f"User (id={self.id}, first_name={self.ft_name}, full_name:{self.fl_name})"

class Address(data_base):
    __tablename__ = "Address"
    id = Column(Integer, primary_key=True, autoincrement = True)
    email_address = Column (String(40), nullable=False) # Não poderá ter campos nulos
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses" )
    # OPCIONAL: construtor para usar argumentos posicionais
    def __init__(self,user_id, email_address):
        self.user_id = user_id
        self.email_address = email_address    
    def __repr__(self): # Método especial 'repr' representando a classe Address, ENTIDADE.
        return f"Address (id={self.id}, e-mail={self.email_address})"


# SQL Alchemy permite parâmetros posicionais, sendo desnecessários o uso abaixo para testes:
#candidato_1 = User(id=1,ft_name="Daniel",fl_name="Martins")
#print(candidato_1)        
# SQL Alchemy permite parâmetros posicionais
candidato_2 = User(2,"Daniel","Martins")
print(candidato_2)
candidato_1= Address(1,"daniel@gmail.com")
candidato_2= Address(2,"thiago@gmail.com")
print(candidato_1)
print(candidato_2)

# Resultados da tela:

User (id=1, first_name=Daniel, full_name:Martins)
User (id=2, first_name=Daniel, full_name:Martins)
Address (id=None, e-mail=daniel@gmail.com)
Address (id=None, e-mail=thiago@gmail.com)

# O ID está saindo 'None' porque não há um banco de dados. Somente tabelas.


