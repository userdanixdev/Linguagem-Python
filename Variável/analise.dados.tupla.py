# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
#em um tupla. E no final,mostre:
#a) Quantas vezes apareceu o valor 9.
#b) Em que posição foi digitado o primeiro valor 03.
#c) Quais foram os números pares.

    #versão 1

num = (int(input('Digite um número: ')),   # para transformar em uma TUPLA , ponha mais parênteses externos.
        int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f' Você digitou os valores {num}.')  # Guardados na tupla
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}°posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f' Os valores pares digitados foram', end='')
for n in num:
    if n%2==0:
        print(n, end='')

