import sqlite3
from  pathlib import Path

# Criar dentro da pasta 
ROOT_PATH = Path(__file__).parent 

# Conexão com o banco de dados:
conection = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
# declarar uma variável para o executar os comandos da conexão
cursor = conection.cursor() 

def criar_tabela(conection,cursor):
    cursor.execute("CREATE TABLE clientes (ID INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100),email VARCHAR(150))")
    conection.commit()
# Inserindo registros: 
def inserir_registro(conection,cursor,nome,email):
    data = (nome,email)
    cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?);",data)
    conection.commit()
def atualizar_registro(conection,cursor,nome,email,ID):
    data =(nome,email,ID)
    cursor.execute("UPDATE clientes SET nome=?,email=? WHERE ID=?;",data)    
    conection.commit()
def excluir_registro(conection,cursor,id):
    data=(id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;",data)
    conection.commit()

excluir_registro(conection,cursor,1)    
#atualizar_registro(conection,cursor,"Geovana","geo@gmail.com",2)    
