# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
#em um tupla. E no final,mostre:
#a) Quantas vezes apareceu o valor 9.
#b) Em que posição foi digitado o primeiro valor 03.
#c) Quais foram os números pares.

#versão 03:

n1=int(input('Digite p 1°numero: '))
n2=int(input('Digite p 2°numero: '))
n3=int(input('Digite p 3°numero: '))
n4=int(input('Digite p 4°numero: '))
cont = 0
tupla=(n1,n2,n3,n4)
for n in tupla:
    par = n % 2
    if par == 0:
        cont = cont + 1
if 9 in tupla:        
    print(f'O número 9 apareceu {tupla.count(9)} vezes.')
else:
    print('O nove, número, 9, não apareci.')
if 3 in tupla:
    print('O number 3 apareceu na {tupla.index(9)+1}°posição.')
else:
    print('Não há valor 3 computado.')
print(f'Aparecerem {cont} valores pares.')
print(f'Os valores pares foram: ',end='')
for n in tupla:
    if n % 2 ==0:
        print(n,end=', ')






