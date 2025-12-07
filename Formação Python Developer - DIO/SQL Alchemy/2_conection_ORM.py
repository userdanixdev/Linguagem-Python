# 2º Conexão com SQL Alchemy via Python.
# A 2º versão será instanciada via argumentos posicionais
# Para isso os parâmetros serão alterados.
# ATENÇÃO! Podemos instanciar um objeto SQLAlchemy usando apenas argumentos posicionais, 
# sem precisar nomear cada atributo feita pela 1º conexão.

# pip install sqlalchemy
import sqlalchemy 
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeiggnKey



