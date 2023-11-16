#Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# 1°parte: ler o nome e peso das pessoas e guardar na lista:

temp=[]         #lista temporária:
principal=[]   #Lista principal
maior=menor=0  # 3°parte ##
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(principal) == 0:
        maior=menor= temp[1]    #  temp[1] é o PESO
    else:
        if temp[1]> maior:
            maior=temp[1]
        if temp[1]< menor:
            menor=temp[1]
    principal.append(temp[:])  # armazenar dentro de outra lista
    temp.clear()                # Para limpar a lista temporária
    resposta=input(' Quer continuar? [S/N] ')
    if resposta in 'Nn':
        break
print('+'*40)    
print(f'Os dados foram {principal}.')

## Parte 02: Quantas pessoas cadastradas:
print(f' Ao todo, você cadastrou {len(principal)} pessoas.')  # Pode criar um contador ou o 'len'
    
## Parte 03: Listagem das pessoas mais pesadase e leves:
print(f'O maior peso foi de {maior}KG,peso de ', end='')
for p in principal:             # Necessário um laço para a listagem: 'p1' é peso, 'p0' é nome
    if p[1] == maior:
        print(f'{p[0]}.', end='')
print(f'O menor peso foi de {menor}KG.')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} ', end='')

