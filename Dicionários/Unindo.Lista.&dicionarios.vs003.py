#Unindo dicionários e listas

#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários
#em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

#VERSÃO 003:
#Obs: ÓTIMA VERSÃO
#Dicionário para adicionar os dados com índice
dados=dict()
#Essa é a lista a qual acessaremos todos os dicionários.
users=list()

#Coleta de dados para lista/dict
soma=media=0
while True:
    dados['nome']=input('Nome do usuário: ')
    dados['idade']=int(input('Idade do usuário: '))
    soma += dados['idade']
    dados['sexo']=input('Sexo do usuário[M/F]: ').upper().strip()
    while True:
        if dados['sexo'] in 'MF':
            print('Usuário cadastrado com sucesso.')
            break
        else:
            print('ERROR.')
            dados['sexo']=input('Digite um sexo válido[M/F]: ').upper().strip()
    users.append(dados.copy())
    print('-'*10)
    while True:
        resp=input('Deseja continuar [S/N]?').upper().strip()
        if resp in 'SN':
            break
            print('Error!')
    if resp == 'N':
       break

#Expor os dados
print(f'> FOram cadastradas {len(users)} pessoas.')
media=soma/len(users)
print(f' A média de idade é de {media:.0f} anos.')
print(f' As mulheres cadastradas foram:', end='')
for p in users:
    if p['sexo']=='F':
        print(f'[{p["nome"]}]',end='')
print()
print(f'>Os usuários acima da média são: ', end='')
for p in users:
    if p['idade']>media:
        print(f'[{p["nome"]}]', end='')
print()
print('[*] Programa finalizado.')




                  

          


        
    

        
      


