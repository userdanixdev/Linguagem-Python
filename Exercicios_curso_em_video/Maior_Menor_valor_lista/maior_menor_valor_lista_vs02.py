# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Versão 02:

lista = []
for c in range(0,5):
    numero = int(input(f'Digite um número para a posição {c+1}: '))
    lista.append(numero)
numero_max = max(lista)
numero_min = min(lista)
print(f'Os valores digitados foram: {lista}.')
print(f'O maior valor digitado foi: {max(lista)} e a sua posição é: {lista.index(numero_max)+1}')
print(f'O menor valor digitado foi: {min(lista)} e a sua posição é: {lista.index(numero_min)+1}')
