#Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

#versão 05:

contador=0
n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
n3=int(input('O terceiro: '))
n4=int(input('Por fim, o quarto: '))
tupla=(n1,n2,n3,n4)
print(f'Os números digitaod foram {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
       print(f'O número 3 aparece primeira na posição {tupla.index(3)+1}.')
else:
    print('Não há número 3.')

for par in tupla:
    if par%2 ==0:
        contador += 1
        print(f'Número pares: {par}')
    else:
        print('Não há nenhum número par.')
        break
