# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
#em um tupla. E no final,mostre:
#a) Quantas vezes apareceu o valor 9.
#b) Em que posição foi digitado o primeiro valor 03.
#c) Quais foram os números pares.

#versão 02:
# Code comprehension #

valores=tuple(int(input('Digite valores:'))for c in range(1,5))
print(f'O número nove aparece {valores.count(9)}vezes' if 9 in valores else 'Não foi digitado o valor 9')
print(f'O valor 3 foi digitado na {valores.index(3)+1}°posição'if 3 in valores else 'Não foi digitado o valor 3')
print('Valores pares digitados foram',end='')
print({n for n in valores if n % 2 == 0},end='')
