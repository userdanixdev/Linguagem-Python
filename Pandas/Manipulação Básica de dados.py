import pandas
pandas.__version__

# Dicionário:
dados_dict = {'Estado': ['Santa Catarina','Rio de janeiro','Tocantins','Bahia',
                        'Minas Gerais'], 
             'ANO':[2004,2005,2006,2007,2008],
             'Taxa Desemprego':[1.5,1.7,1.6,2.4,2.7]}
type(dados)
dados = pandas.DataFrame(dados)
type(dados)
dados.head()
# Reorganizando as colunas:
pandas.DataFrame(dados,columns=['ANO','Estado','Taxa Desemprego'])    
dados.head()
dados = pandas.DataFrame(dados,columns=['ANO','Estado','Taxa Desemprego'])

# Criando outro dataframe com os mesmos dados anteriores mas add uma coluna:
dados_2 = pandas.DataFrame(dados_dict,columns=['Estado','Taxa Desemprego','Taxa Crescimento',
                                               'ANO'],
                           index=['estado1','estado2','estado3','estado4','estado5'])
dados_2.
# Para imprimir somente uma coluna no console basta digitar o código abaixo:
dados_2['Estado']
# Para imprimir somente duas colunas, atenção aos parênteses duplos:
dados_2[['Estado','ANO']]    
### NaN = Not Number ###
dados_2.values
dados_2.dtypes
dados_2.columns
### RESUMO ESTATÍSTICO DO DATAFRAME:
dados_2.describe()  
# Visualização geral da base de dados:  
display(dados_2.info())
#  Verificação de valores nulos, ausentes, não avaliados:
dados_2.isna()    
# usando a biblioteca numpy para preencher números nulos, não avaliados ou ausentes:
import numpy
dados_2['Taxa Crescimento']=numpy.arange(5. )
dados_2.isna()
# todos os dados preenchidos
##############################################
# Preenchendo valores nulos, ausentes em dataframes no Pandas:

dsa_df =pandas.read_csv('C:\Python_DSA\Cap10\dataset.csv')
# Verificar os dados contidos no arquivo
dsa_df.dtypes
dsa_df.describe()
# Verificar se contem dados nulos e fazer uma soma deles:
dsa_df.isna().sum()
# Ao verificar qual tabela com as funções acima, no caso a tabela: Quantidade
# Fazer a interpolação de dados para preencher dados nulos ou não avaliados:
    # Extrair a moda da coluna 'Quantidade'
moda=dsa_df['Quantidade'].value_counts().index[0]
print(moda)
# O valor da moda da tabela 'Quantidade' é 3.0
# Com esse resultado , preencher os dados nulos com esse valor:
dsa_df['Quantidade'].fillna(value=moda,inplace=True)
dsa_df['Quantidade']
# Conferir novamente com o comando anterior sobre os valores nulos:
dsa_df.isna.sum()

