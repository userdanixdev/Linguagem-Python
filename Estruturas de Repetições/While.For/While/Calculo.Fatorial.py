#Faça um programa que leia um número qualquer e mostre o seu fatorial:

#Exemplo 01 (Simplificado)- Por módulos:

from math import factorial
n=int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')



#Exemplo 02:

n=int(input('Digite um número para calcular o fatorial: '))
c=n
f=1 
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c> 1 else '=',end='')
    f = f*c
    c = c - 1
print(f'{f}.')
Results:
Digite um número para calcular o fatorial: 12
12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1=479001600.
=============================================================================

