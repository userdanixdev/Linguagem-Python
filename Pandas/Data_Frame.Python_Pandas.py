# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:19:49 2024

@author: US
"""
import pandas as pd


# Carregando dataset
data = pd.read_csv('C:/Users/jessi/Downloads/GasPricesinBrazil_2004-2019.csv', sep=';')
# necessário utilizar um separador correto, por padrão é vírgula
data.head()
# Exibição das linhas 5 por padrão, pode colocar quantas linhas quiser dentro dos parênteses
data.info()
# Mostra as informações do tipos de dados e o conteúdo das colunas
# Data Frame:
# Todo dataset carregado ( dados estruturados ) é um data frame : tabela bi-dimensional mutável com dado variados
### PARA VERIFICAR SE É BASTA DIGITAR:
type(data) 
# As dimensões do data frame utilizando um atributo:
data.shape    
# ( Primeiro: Nº de linhas, Segundo: COLUNAS)
print(f'O DataFrame do arquivo lido em CSV possui {data.shape[0]} linhas/observações/registros \n e \n{data.shape[1]} colunas/atributos/variáveis')
                
                  
    
#####################################################################
OK
