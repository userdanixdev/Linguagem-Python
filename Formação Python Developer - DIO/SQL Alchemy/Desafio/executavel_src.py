import os

def criar_pasta(path):
    """Cria a pasta se não existir."""
    os.makedirs(path, exist_ok=True)
    print(f"Pasta criada ou já existente: {path}")

def criar_arquivo(path, conteudo=""):
    """Cria um arquivo com o conteúdo fornecido (pode ser vazio)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"Arquivo criado: {path}")

def criar_estrutura_projeto(raiz_projeto):
    """Cria a estrutura src com __init__.py e database.py."""
    
    # Caminho da pasta src
    src_path = os.path.join(raiz_projeto, "src")
    
    # Criar src
    criar_pasta(src_path)
    
    # Criar __init__.py (vazio)
    init_file = os.path.join(src_path, "__init__.py")
    criar_arquivo(init_file)
    
    # Criar database.py com Base do SQLAlchemy
    database_file = os.path.join(src_path, "database.py")
    database_content = """\
from sqlalchemy.orm import declarative_base

# Base para todos os modelos do SQLAlchemy
Base = declarative_base()
"""
    criar_arquivo(database_file, database_content)
    
    print("\nEstrutura do projeto criada com sucesso!")
    print(f"- Pasta: {src_path}")
    print("- Arquivos: __init__.py, database.py")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    raiz_do_projeto = r"userdanixdev/Linguagem-Python/Formação Python Developer - DIO/SQL Alchemy/Desafio"
    criar_estrutura_projeto(raiz_do_projeto)
