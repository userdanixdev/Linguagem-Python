# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Versão 01:

lista = []  # Entre parênteses é lista
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição: {c+1}.')))   # Adiciona os valores do usuário a lista 'append'
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valores {lista}.')    
print(f'O maior valor foi: {maior} nas posições ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()        
print(f'O menor valor foi: {menor} nas posições ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print()        
