# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Versão 1:

numero = (int(input('Digite um número: ')),
          int(input('Digite segundo número: ')),
          int(input('Digite terceiro número: ')),
          int(input('Digite quarto número: ')))

print(f'Você digitou os valores {numero}.')
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f' O valor 3 apareceu na {numero.index(3)+1} posição.')
else:
    print('O valor digitado não apareceu.')
print('Os valores digitados pares digitados foram: ')    
for n in numero:
    if n % 2 == 0:
        print(n)

        

