#Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

valores=tuple(int(input('Digite valores:'))for c in range(1,5))
print(f'O número nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}°posição'if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram',end='')
print({n for n in valores if n%2==0},end='')
