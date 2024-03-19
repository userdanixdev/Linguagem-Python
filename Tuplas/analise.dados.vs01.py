# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
#em um tupla. E no final,mostre:
#a) Quantas vezes apareceu o valor 9.
#b) Em que posição foi digitado o primeiro valor 03.
#c) Quais foram os números pares.

numeros=(int(input('Digite um número: ')),
             int(input('Digite um número: ')),
                 int(input('Digite um número: ')),
                     int(input('Digite um número: ')))
print(f'Voce digitou os valores {numeros}.')
if 9 in numeros:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
else:
    print('O valor 9 não apareceu em nenhum valor imputado.')        
# Em que posição foi digitado o valor 3?
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}° posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
    # Quais valores pares?
print(f'Os valores pares digitam foram:',end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n,end=' ')
