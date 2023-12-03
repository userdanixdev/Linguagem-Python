#Unindo dicionários e listas

#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários
#em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

#VERSÃO 002:

pessoas={}
cadastro={}
tot=0
while True:
    cadastro['nome']=input('Nome: ').capitalize()
    while True:
        sexy=input('Sexo: ').upper()
        if sexy in 'MF':
            cadastro['sexo']= sexy
            break
        else:
            print('Erro. Responda apenas M ou F.')
            continue
    cadastro['idade']=int(input('Idade: '))
    pessoas[cadastro["nome"]]=cadastro.copy()
    while True:
        resp=input('Quer continuar?[S/N]: ').upper()
        if resp in 'SN':
            break
        print('Erro. Responda apenas S ou N.')
    if resp in 'N':
        break
print(f'A) Ao todo foram cadastradas {len(pessoas)} pessoas')
for key,value in pessoas.items():
    tot += value['idade']
media=tot/len(pessoas)
print(f'B) A média da idade é {media:.2f}')
print(f'C) As mulheres cadastradas foram ')
for k, v in pessoas.items():
    if v['sexo'] in 'F':
        print(f'{k,}',end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for key, value in pessoas.items():
    if value['idade']>=media:
        print(f'Nome={key};sexo={value["sexo"]};idade={value["idade"]};')
   


        
    

        
      


