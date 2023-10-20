#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista.

#Versão 02:

valores=[]
for contador in range(0,5):
    valores.append(int(input('Digite número: ')))
print(f'Os números digitados foram: {valores}')
print(f'O maior número foi {max(valores)} na(s) posição(ões): ',end='')
for maior in range(0,5):
    if valores[maior] == max(valores):
        print(f'{maior+1}°', end='')
print(f'\nO menor número foi {min(valores)} na(s) posição(ões):',end='')
for menor in range (0,5):
    if valores[menor] == min(valores):
        print(f'{menor+1}°',end='')





