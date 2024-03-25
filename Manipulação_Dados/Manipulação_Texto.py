# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:30:05 2024

@author: US
"""
# Abrindo o arquivo para leitura, obrigatório o uso dos parâmtros de codificação das strings
# E o modo como será aberto: Leitura ou Gravação
open(file="C:/Users/jessi/OneDrive/Área de Trabalho/arquivo.txt",encoding='utf-8',mode='r')

#O arquivo acima, não foi declarado nenhuma variável, sendo assim:
arquivo =open(file="C:/Users/jessi/OneDrive/Área de Trabalho/arquivo.txt",encoding='utf-8',mode='r')

arquivo.read(10)
arquivo.seek(0,0)
arquivo.tell()
# Esse arquivo não existe, foi criado em modo ESCRITA, ou seja, WRITE:
arquivo_2 =open(file="C:/Users/jessi/OneDrive/Área de Trabalho/arquivo_2.txt",encoding='utf-8',mode='w')
arquivo_2.write("Estou aprendendo Python")
# Para eu poder LER o arquivo criado, primeiramente, devemos fechá-lo:
arquivo_2.close()
# Agora abaixo, ler o arquivo gravado:
arquivo_2=open(file="C:/Users/jessi/OneDrive/Área de Trabalho/arquivo_2.txt",encoding='utf-8',mode='r')    
arquivo_2.read()
# Como agora o arquivo está em somente LEITURA, podemos acrescentar conteúdo com o método 'a' de append:
arquivo_2=open(file="C:/Users/jessi/OneDrive/Área de Trabalho/arquivo_2.txt",encoding='utf-8',mode='a')    
# Agora o arquivo está pronto para ser inserido dados:
arquivo_2.write("E a metodologia de ensino da DSA facilita meu aprendizado")    
# Feche o arquivo para leitura posterior:
arquivo_2.close()    
arquivo_2=open(file="C:/Users/jessi/OneDrive/Área de Trabalho/arquivo_2.txt",encoding='utf-8',mode='r')
arquivo_2.read()

#######################################################################################################
# Manipulação de dados REAIS:
f = open('C:/Users/jessi/Downloads/Current_Employee_Names__Salaries__and_Position_Titles_20240325.csv','r')    
# O arquivo original está em texto tamanho único, csv
# Declarando uma variável para o arquivo, ele se torna mais mutável
data = f.read()
# Com a função split dividimos todas as linhas em uma única lista
rows = data.split('\n')
    for row in rows:
        split_row = row.split(',')
        full_data.append(split_row)
        
