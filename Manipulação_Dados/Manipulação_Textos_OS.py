# Manipulação de Textos com o pacote 'OS' - Operational System - :

texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser proficientes em data Science."
print(texto)
import os
# Criação do arquivo de gravação com o pacote Operation System:
arquivo = open(os.path.join("C:/Users/jessi/OneDrive/Área de Trabalho/arquivo_1.txt"),"w")   
 # Gravando os dados no arquivo:
for palavra in texto.split():
    arquivo.write(palavra + ' ')    
arquivo.close()   
# Leitura do arquivo
arquivo = open('C:/Users/jessi/OneDrive/Área de Trabalho/arquivo_1.txt','r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)               


