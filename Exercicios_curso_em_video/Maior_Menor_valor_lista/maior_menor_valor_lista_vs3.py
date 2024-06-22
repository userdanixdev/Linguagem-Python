# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Versão 03:

valores = []
for c in range(0,5):
    numero = int(input(f'Digite um número para a posição {c+1}: '))
    valores.append(numero)
print(f'Os valores digitados foram: {valores}.')
print(f'O maior valor digitado foi: {max(valores)} e a sua posição é: {valores.index(min(valores))+1}')
print(f'O menor valor digitado foi: {min(valores)} e a sua posição é: {valores.index(max(valores))+1}')
