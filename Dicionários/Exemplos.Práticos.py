

# DICIONÁRIOS EM PYTHON:
pessoas={'nome': 'Gustavo', 'sexo':'M', 'idade':22}  	# Como informado acima, dicionário declara com chaves: '{}'
print(pessoas)
# Para declarar usa chaves, para referência usa-se colchetes. ATENÇÃO! A referência, deve ser de aspas duplas.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
#Resposta no console: dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())
# Resposta no console: dict_values(['Gustavo', 'M', 22])
print(pessoas.items())
# Resposta no console: dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
# Podemos acessar chaves, valores e elementos por laços:
for k in pessoas.keys():
    print(k)
# Resposta no console:
#nome
#sexo
#idade
for k, v in pessoas.items():
    print(f'{k} = {v}')    # No dicionário devemos usar o items e não enumerate.
# Resposta no console:
#nome = Gustavo
#sexo = M
#idade = 22
# ATENÇÃO: Não precisa de usar .append em dicionário, basta acrescentar usando colchetes da forma abaixo:
pessoas['peso']= 98.5
print(pessoas.items())
#Resposta no console:
#dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22), ('peso', 98.5)])

#Exemplo Prático 02:
brasil=[]    # Lista
estado1 = {'UF':'Rio de Janeiro','Sigla':'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)   # Como dicionário, conforme declarado acima
print(estado2)  # Como dicionário, conforme declarado acima.
# Resposta no console:
#{'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
#{'UF': 'São Paulo', 'Sigla': 'SP'}

# Dicionário dentro de uma lista:
print(brasil)   #<- Lista com os dicionários
# Resposta no console: [{'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}, {'UF': 'São Paulo', 'Sigla': 'SP'}]
# AGORA EU TENHO UMA LISTA COM OS DICIONÁRIO DENTRO DESSA LISTA BRASIL.

# OUTRO EXEMPLO PRÁTICO:
estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF']= str(input('Unidade federativa: '))
    estado['Sigla']= str(input('Sigla do Estado: '))
    #brasil.append(estado)    # brasil é uma lista, portanto, pdoemos usar a função.
    brasil.append(estado.copy())
#print(brasil)
# Rsposta no console: [{'UF': 'AC', 'Sigla': 'DF'}, {'UF': 'AC', 'Sigla': 'DF'}, {'UF': 'AC', 'Sigla': 'DF'}]
# ATENÇÃO REPARE QUE PRECISAMOS FATIAR, PQ A SIGLA REPETIU TODOS. NA LISTA PRECISAMOS COPIAR OS DADOS
#  brasil.append(estado.copy())
for e in brasil:  # Laço para a lista
    print(e)    # 'e' é do dicionário
#Resultado no console abaixo:
#{'UF': 'Brasilia', 'Sigla': 'DF'}
#{'UF': 'Sao Paulo', 'Sigla': 'SP'}
#{'UF': 'Parana', 'Sigla': 'PR'}
for e in brasil:
    for k,v in e.items():   
        print(f'O campo {k} tem valor {v}.')   # formatado
#Resultado do console abaixo:
#O campo UF tem valor Brasilia.
#O campo Sigla tem valor DF.
#O campo UF tem valor Sao Paulo.
#O campo Sigla tem valor SP.
#O campo UF tem valor Parana.
#O campo Sigla tem valor PR.
        
