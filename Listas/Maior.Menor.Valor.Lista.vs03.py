#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista.

#Versão 03:

valores=[]

for contador in range(0,5):
    valores.append(int(input('Digite número: ')))
print(f'Os números digitados foram: {valores}')
print(f'O maior número foi {max(valores)} na(s) posição(ões): {valores.index(max(valores))}°') 
print(f'O menor número digitado é: {min(valores)} na posição {valores.index(min(valores))}°')

Results:

Digite número: 15
Digite número: 25
Digite número: 20
Digite número: 20
Digite número: 21
Os números digitados foram: [15, 25, 20, 20, 21]
O maior número foi 25 na(s) posição(ões): 1°
O menor número digitado é: 15 na posição 0°

================================================================




