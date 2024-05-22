# Unindo dicionários e listas

# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

# VERSÃO 005:
# Dicionário para adicionar os dados com índice:
dados=dict()
# Essa é a lista a qual acessaremos todos os dicionários:
users=list()
# Coleta de dados para lista/dict:
soma = 0
media = 0
while True:
  dados['nome']=input('Nome do usuário: ') # Dicionário dados recebe chave 'nome' e input com um valor
  while True:   # Looping para retornar quando vier um erro
    try:
      dados['idade']=int(input('Idade do usuário: '))
      soma += dados['idade']
      break
    except valor_error:
      print('Por favor, insira um número válido.')
print(f'Idade registrada: {dados['idade']}')
dados['sexo']=input('Sexo do usuário [M/F]: ').upper().strip()
while True:
  resp=input('Desejas continuar [S/N]? ').upper().strip()
  if resp in 'SN':
    break
    print('ERROR')
if resp == 'N':
    break

# Expor os dados:
print(f' Foram cadastradas {len(users)} pessoas.')
media=soma/len(users)
print(' A média de idade é de {media:.0f} anos.')
for p in users:


