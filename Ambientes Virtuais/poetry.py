## Poetry é outra ferramenta de gerenciamento de dependências para Python, concorrente do pipenv que permite declarar bibliotecas do seu projeto dentro de um ambiente virtual
# que permite gerenciar para você.
# Tambem pode disponibilizar pacotes dentro do PyPI.

## Para instalar:
pip install poetry  # Para instalar
poetry new myproject # Para criar um novo projeto
cd myproject # Entrar no projeto em ambiente virtual
poetry add numpy  # Adicionar dependência
poetry remove numpy # Remover dependência

## Poetry init vai fazer o pacote inicializar e gerenciar seu projeto:

poetry init

This command will guide you through creating your pyproject.toml config.

Package name [.env]:  project_poetry
Version [0.1.0]:  
Description []:  Teste com poetry
Author [Daniel <f.daniel.m@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [^3.12]:  

Would you like to define your main dependencies interactively? (yes/no) [yes]

You can specify a package in the following forms:                           ]
  - A single name (requests): this will search for matches on PyPI
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Package to add or search for (leave blank to skip): django
Found 20 packages matching django
Showing the first 10 matches

Enter package # to add, or the complete package name if it is not listed []: [ 0] Django
 [ 1] django4django
 [ 2] django-503
 [ 3] django-filebrowser-django13
 [ 4] django-cryptography-django5
 [ 5] django-fsm-admin-django-4
 [ 6] django-graphql-auth-django-4
 [ 7] django-totalsum-admin-django3
 [ 8] django-debug-toolbar-django13
 [ 9] django-django_csv_exports
 [ 10]
 >

Enter the version constraint to require (or leave blank to use the latest version): 
Using version ^0.0.2 for django4django

Add a package (leave blank to skip): 

Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "project-poetry"
version = "0.1.0"
description = "Teste com poetry"
authors = ["Daniel <f.daniel.m@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
django4django = "^0.0.2"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"




