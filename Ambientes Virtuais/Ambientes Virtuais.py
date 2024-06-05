## Ambientes virtuais nos permitem manter dependênciias de diferentes projetos. Importante para evitar conflitos entre versões de pacotes ##
## Para criar um ambiente virtual é necessário os seguintes passos:
## No terminal do seu computador crie uma pasta para ambiente virtual:
  ## 
PS C:\Users\jessi> mkdir Manipulacao_arquivos


    Diretório: C:\Users\jessi


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        05/06/2024     15:58                Manipulacao_arquivos 

## Ao criar a pasta, entre nela:
  # PS C:\Users\jessi\Manipulacao_arquivos> 
Nesta pasta crie outra com o nome 'Ambiente_Virtual':
PS C:\Users\jessi\Manipulacao_arquivos\Ambiente_Virtual> 
## Dentro dessa pasta digite:
python -m venv .env
## Ao listar a pasta criada, estará incluso os seguintes arquivos:
PS C:\Users\jessi\Manipulacao_arquivos\Ambiente_Virtual> ls .env


    Diretório: C:\Users\jessi\Manipulacao_arquivos\Ambiente_Virtual\.env


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        05/06/2024     16:04                Include
d-----        05/06/2024     16:04                Lib
d-----        05/06/2024     16:04                Scripts
-a----        05/06/2024     16:04            342 pyvenv.cfg

## Para ativar o ambiente virtual:
nome_do_ambiente\Scripts\activate.bat

## No vscode utilize o atalho Crtl + Shift + P e escolher Python Enviroment:


