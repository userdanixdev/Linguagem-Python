#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista.

listanum=[]   # ou colocar list()
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    # Para colocar valores na lista 'listnum' é necessário colocar o método 'append'
print('+'*50)
print(f' Você digitou os valores {listanum}')

'''Resultado:
Digite um valor para a posição 0: 10
Digite um valor para a posição 1: 11
Digite um valor para a posição 2: 12
Digite um valor para a posição 3: 13
Digite um valor para a posição 4: 14
++++++++++++++++++++++++++++++
 Você digitou os valores [10, 11, 12, 13, 14]'''
# Fizemos a primeira parte do exercício. Ler os 5 valores e guardar na lista.

# Segunda parte:
        # - Mostrar qual o MAIOR E O MENOR - #
     
maior = 0
menor = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f' Você digitou os valores {listanum}')            
print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')

'''Resultado geral:
    Digite um valor para a posição 0: 1
Digite um valor para a posição 1: 2
Digite um valor para a posição 2: 3
Digite um valor para a posição 3: 4
Digite um valor para a posição 4: 5
++++++++++++++++++++++++++++++++++++++++++++++++++
 Você digitou os valores [1, 2, 3, 4, 5]
Digite um valor para a posição 0: 45
Digite um valor para a posição 1: 46
Digite um valor para a posição 2: 47
Digite um valor para a posição 3: 48
Digite um valor para a posição 4: 49
 Você digitou os valores [1, 2, 3, 4, 5, 45, 46, 47, 48, 49]
O maior valor digitado foi 5.
O menor valor digitado foi 1.'''

# Colocar nas posições devidas:
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f' Você digitou os valores {listanum}')            
print(f'O maior valor digitado foi {maior} nas posições: ',end='') ## POSIÇÃO ##
for i, v in enumerate(listanum):   # 'i' para ÍNDICE & 'v' para VALOR
    if v == maior:
        print(f'{i}°...',end='')      
print(f'\nO menor valor digitado foi {menor} na posição: ',end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}°...',end='')

'''Resultados gerais:
    Digite um valor para a posição 0: 1
Digite um valor para a posição 1: 2
Digite um valor para a posição 2: 3
Digite um valor para a posição 3: 4
Digite um valor para a posição 4: 5
++++++++++++++++++++++++++++++++++++++++++++++++++
 Você digitou os valores [1, 2, 3, 4, 5]
Digite um valor para a posição 0: 1
Digite um valor para a posição 1: 2
Digite um valor para a posição 2: 3
Digite um valor para a posição 3: 4
Digite um valor para a posição 4: 5
 Você digitou os valores [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
O maior valor digitado foi 5.
O menor valor digitado foi 1.
Digite um valor para a posição 0: 1
Digite um valor para a posição 1: 2
Digite um valor para a posição 2: 3
Digite um valor para a posição 3: 4
Digite um valor para a posição 4: 5
 Você digitou os valores [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
O maior valor digitado foi 5 nas posições: 4°...9°...14°...
O menor valor digitado foi 1 na posição: 0°...5°...10°...'''
===================================================================

        
            








