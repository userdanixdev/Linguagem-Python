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
                
                    ### CRIANDO UM DATAFRAME ###

jogadores_df = pd.DataFrame({
    'Nome':['Ronaldo','Ronaldinho','Kaká','Adriano','Juninho Pernambucano'],
     'Idade':[30,28,28,26,31],
      'Peso': [98.5,75,78,85,72],
      'Posição':['Atacante','Meio-campo','Meio campo','Atacante','Meio campo']})                    
                    
jogadores_df.info()
# informações do dataframe criado
jogadores_df.columns
## Esse método mostra somente as colunas do data frame
list(jogadores_df.columns)                    
## Irá mostrar as colunas em lista, por exemplo.
jogadores_df_renomeado = jogadores_df.rename(columns={
     'Nome': 'Nome Apelidado',
      'Idade':'Idades' })
jogadores_df_renomeado.info()
print(jogadores_df_renomeado           )
#################################################
jogadores_df.rename(columns={'Nome': 'Nome Apelidado',
      'Idade':'Idades' }, inplace=True)
jogadores_df #<- Sendo assim, outra forma de renomear a coluna é com o 'inplace'
#####################################################################
# OUTRA FORMA DE RENOMEAR COLUNAS DE UMA VEZ:
jogadores_df.columns = ['NOME', 'IDADE', 'PESO','POSIÇÃO']    
jogadores_df
#####################################################################
