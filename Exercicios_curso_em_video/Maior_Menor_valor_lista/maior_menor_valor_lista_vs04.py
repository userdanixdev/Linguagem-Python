# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Versão 04:

a = [input(f'Digite um valor para a posição {i+1}: ')for i in range(0,5)]
posmax = []
posmin = []
for pos,valor in enumerate(a):
    if valor == max(a):
        posmax.append(pos)
    elif valor == min(a):
        posmin.append(pos)
print(f'O maior valor foi {max(a)} e está na posição {posmax}')
print(f'O menor valor foi {min(a)} e está na posição {posmin}')

