# Versão 005:
dados=dict()
users=list()
soma = 0
media = 0
while True:
  dados['nome']=input('nome do usuário: ')
  while True:
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
print(f' A média de idade é de {media:.0f} anos. ')
for p in users:    # Looping em que para cada chave 'p' em usuários imprime o valor do dicionário 'nome'
  if p['sexo']=='F':
    print(f' As mulheres cadastradas foram: ',[{p["nome"]}])
print()
usuarios_acima_da_media = []
for p in users:  # Loop para cada chave como 'p' dentro do dicionário 'users'
  if p['idade'] > media:  # Se o valor da chave 'idade' for maior que a média
    usuarios_acima_da_media.append(p['nome'])  # Adiciona o nome do usuário a lista
# Verifica se a lista não está vazia:
if usuarios_acima_da_media:
  print('Os usuários acima da média são:', ', '.join(usuarios_acima_da_media))
else:
  print('Nenhum usuário acima da média.')

dados=dict()
# Essa é a lista a qual acessaremos todos os dicionários
users=list()
# Coleta de dados para lista/dict:
soma = 0
media = 0
while True:
  dados['Nome']=input('Nome do usuário: ')         # Dicionário recebe chave nome e imput com um valor 
  dados['idade']=int(input('Idade do usuário: '))  # Dicionário dados recebe chave 'idade' e input a ser inserido
  soma += dados['idade']
  dados['sexo']=input('Sexo do usuário [M/F]: ').upper().strip()
  while True:
    if dados['sexo'] in 'MF':
      print('Usuário cadastrado com sucesso.')
      break
    else:      
      print('ERROR')
      dados['sexo']=input('Digite um sexo válido [M/F]: ').upper().strip()
  users.append(dados.copy())   
  print('='*10)
  while True:
    resp=input('Desejas Continuar [S/N]?').upper().strip()
    if resp in 'SN':
      break
      print('ERROR')
  if resp == 'N':
    break

# Expor os dados: 
print(f' Foram cadastradas {len(users)} pessoas.')
media=soma/len(users)
print(f' A média de idade é de {media:.2f} anos.')
print(f' As mulheres cadastradas foram: ', end='')
for p in users:     # Looping em que para cada chave 'p' em usuários imprime o valor do dicionário 'nome'
  if p['sexo']=='F':
    print(f'[{p["Nome"]}]',end='')
print()
print(f' Os usuários acima da média são: ',end='')
for p in users:  
  if p['idade']>media:
    print(f'[{p["nome"]}]', end='')

print()
print('Programa finalizado')



