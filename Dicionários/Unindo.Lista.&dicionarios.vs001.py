#Unindo dicionários e listas

#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários
#em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

#VERSÃO 001:

#pessoa=dict()    # o .clear não precisa para dicionários, os valores vão sendo substituidos.

dic={}
pessoas=[]
media=0
while True:
    dic['Nome']=input('Nome: ').strip().title()
    dic['Idade']=int(input('Idade: '))
    dic['Sexo']=input('Sexo: [M/F]').strip().upper()[0]
    while dic['Sexo']!='M' and dic['Sexo']!='F':
        dic['Sexo']=input('Decisão inválida. Sexo somente [M/F]: ').upper()[0]
    pessoas.append(dic.copy())
    decision=input('Deseja continuar o cadastro? [S/N]').upper()[0]
    while decision != 'S' and decision !='N':
        decision=input('Decisão inválida. Deseja continuar?[S/N]').upper()[0]
    if decision in 'Nn':
        break
    for v in range(0,len(pessoas)):
        media += pessoas[v]["Idade"]
print(f'A) O total de pessoas cadastradas foram {len(pessoas)}.')
print(f'B) A média das idades foram {media/len(pessoas):.2f}.')
print(f'C) As mulheres cadastradas foram: ', end=' ')
for v in range(0,len(pessoas)):
    #media += pessoas[v]["Idade"]
    if pessoas[v]["Sexo"]=='F':
        print(f'{pessoas[v]["Nome"]}',end='')
print()
print('D) A lista de pessoas com idade acima da média: ')
for v in range(0,len(pessoas)):
    if pessoas[v]["Idade"]>=media/len(pessoas):
        print(f'Nome:{pessoas[v]["Nome"]}, Idade:{pessoas[v]["Idade"]}, Sexo:{pessoas[v]["Sexo"]}')
print()        




        
    

        
      


