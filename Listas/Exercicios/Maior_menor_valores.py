#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista.

lista=[]
for c in range(1,6):
    lista.append(int(input(f'Digite um valor para a posição {c}°: ')))
print('-'*50)
print(f' O maior número foi {max(lista)}\n',end='')
print(f' O menor número foi {min(lista)}',end='')
print(f' O maior número foi {max(lista)} na posição {lista.index(max(lista))}°')
print(f' O menor número foi {min(lista)} na posição {lista.index(min(lista)+1)}°')

