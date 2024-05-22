# Versão 05.1:
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
soma  = 0
media = 0
while True:
    dados['nome']=input('Nome do usuário: ')         # Dicionário dados recebe chave 'nome' e input com um valor
    while True:
        try:
            dados['idade']=int(input('Idade do usuário: '))
            soma += dados['idade']
            break
        except valor_error:
            print('Por favor, insira um número válido.')            
    print(f'Idade registrada: {dados['idade']}')
    while True:
        dados['sexo']=input('Sexo do usuário[M/F]: ').upper().strip()
        if dados['sexo'] in 'MF':
            break
        else:
            print('Digite  um sexo válido.')
    users.append(dados.copy())  # Adiciona o dicionário a lista de usuários:
    print()            
    while True:
        resp=input('Desejas continuar [S/N]? ').upper().strip()
        if resp in 'SN':
            break
            print('ERROR')
    if resp == 'N':
        break
    
# Expor os dados:
print(f' Foram cadastradas {len(users)} pessoas.')
if len(users) > 0:
    media = soma/len(users)
    print(f'A média de idade é de {media:.2f} anos.')
else:
    print('Nenhuma pessoa foi cadastrada.')
    
for p in users:           # Looping em que para cada chave 'p' em usuários imprime o valor do dicionário 'nome'
    if p['sexo']== 'F':
        print(f' As mulheres cadastradas foram: ',[{p["nome"]}])
print()
#print(f' Os usuários acima da média são: ',end='')
# Está imprimindo 'nenhum usuário acima da média' dentro do loop para cada usuário que não atende a condição em que resulta
# em múltiplas impressões indesejadas. É necessário usar uma flag e fazer a impressão fora do loop.
found=False
for p in users:           # Looping para cada chave como 'p' dentro do dicionários 'users'
   if p['idade']>media:  # Se o valor da chave 'idade' for maior que a média irá mostrar o valor da chave 'nome'
      print(f'Os usuários acima da média são: [{p["nome"]}]')
      found =  True     # A flag como True se encontrar algum usuário acima da média
    
if not found:             # Verifica se a flag ainda é False após o loop
    print('Nenhum usuário acima da média.')

    

    
    
