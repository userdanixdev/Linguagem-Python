#Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

#versão 03:

n1=int(input('Digite o 1°número: '))
n2=int(input('Digite o 2°número: '))
n3=int(input('Digite o 3°número: '))
n4=int(input('Digite o 4°número: '))
cont=0
tupla=(n1,n2,n3,n4)
for n in tupla:
    par=n%2
    if par ==0:
        cont = cont +1
print(f'O número 9 apareceu{tupla.count(9)} vezes.')
if 3 in tupla:
    print('O número 3 apareceu na {tupla.index(3)+1}ºposição.')
else:
    print('Não há valor 3.')
print(f'Apareceram {cont} valores pares.')    
