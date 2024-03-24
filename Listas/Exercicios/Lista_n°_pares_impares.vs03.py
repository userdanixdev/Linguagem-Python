#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Versão 03:

valores=[[],[]]
for contador in range(7):
   number=int(input(f'Digite o {contador+1}° número: '))
   valores[0].append(number) if number % 2 == 0 else valores[1].append(number)
print('+'*22,f'\nNúmeros pares digitados:{sorted(valores[0])}\nNúmeros impares:{sorted(valores[1])}.')
