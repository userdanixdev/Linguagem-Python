# No dataset importado, tem muitas colunas com strings:
# Filtrar o dataframe pela coluna SEGMENTO com valores que iniciam  com as letras 'Con':
dsa_df[dsa_df.Segmento.str.startswith('Con')].head()
# Irá filtrar a coluna 'Segmento', strings que começam com as letras 'Con' e irá mostrar os 5 primeiros.
# Outro exemplo:
dsa_df[dsa_df.ID_Pedido.str.startswith('CA')].head()
# Irá filtrar a coluna 'ID_Pedido' as strings que começam com as letras iniciais 'CA' e irá mostrar os 5 primeiros.
# Filtragem com strings que terminam com tais letras:
dsa_df[dsa_df.Segmento.str.endswith('mer')].head()
# Outro exemplo:
dsa_df[dsa_df.ID_Pedido.str.endswith('966')].head(50)
# pedi para filtrar a coluna 'ID_Pedido' a string com final '966' e mostrar os 50 resultados, porém, com o count()
dsa_df[dsa_df.ID_Pedido.str.endswith('966')].count() # <- temos 11 linhas com essa filtragem.
# Split da coluna pelo caracter('-')
dsa_df['ID_Pedido'].str.split('-').str[1].head()
# Criar uma coluna nova somente com o filtro realizado:
# Engenharia de atributos:
dsa_df['Ano']=dsa_df['ID_Pedido'].str.split('-').str[1]
# Aplicação do group by:
dsa_df[['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).mean()
# Agregação múltipla:
dsa_df[['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).agg(['mean','std','count'])
# Outro exemplo:
dsa_df[dsa_df.ID_Pedido.str.startswith('CA')].head()


# Concatenar Strings:
# 1°Passo: Criar um atribuição com uma nova coluna: 'Pedido_Segmento'
dsa_df['Pedido_Segmento']=dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'],sep='-')

