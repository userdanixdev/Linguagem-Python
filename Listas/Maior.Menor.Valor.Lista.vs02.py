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

Result:

Digite número: 5
Digite número: 6
Digite número: 10
Digite número: 3
Digite número: 33
Os números digitados foram: [5, 6, 10, 3, 33]
O maior número foi 33 na(s) posição(ões): 5°
O menor número foi 3 na(s) posição(ões):4°

========================================================





