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
