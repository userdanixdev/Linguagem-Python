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


