# Conexão com SQL Alchemy via Python.
# Essa 1° versão será instanciada via argumentos nomeados.

# pip install sqlalchemy
import sqlalchemy #as sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


data_base = declarative_base()

class User(data_base):
    __tablename__ = "user_account"
    # Definir coluna, atributos e restrições:
    id = Column(Integer, primary_key=True,autoincrement=True)
    ft_name = Column(String)
    fl_name = Column(String)
    # O correto é nome da propriedade, não o nome da classe na relação no 'back_populates'.
    addresses=relationship("Address", back_populates= "user", cascade="all, delete-orphan")
    def __repr__(self):  # Método especial 'repr' representando a classe USER, ENTIDADE.
        return f"User (id={self.id}, first_name={self.ft_name}, full_name:{self.fl_name})"

class Address(data_base):
    __tablename__ = "Address"
    id = Column(Integer, primary_key=True, autoincrement = True)
    email_address = Column (String(40), nullable=False) # Não poderá ter campos nulos
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    # O correto é nome da propriedade, não o nome da classe na relação no 'back_populates'.
    user = relationship("User", back_populates="addresses" )
    
    def __repr__(self): # Método especial 'repr' representando a classe Address, ENTIDADE.
        return f"Address (id={self.id}, e-mail={self.email_address})"

# Construimos as classes em Python orientada a objeto com métodos ORM para banco de dados relacional.
# Atributos via argumentos nomeados para versão 1.
candidato_1 = User(id=1,ft_name="Daniel",fl_name="Martins")
print(candidato_1)        

