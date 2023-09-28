#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
#Também indique o menor e o maior valor que estão na tupla.

'''como que irei randomizar valores e colocar em uma tupla?'''

from random import randint # randint randomiza números inteiros
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print (f'Os valores sorteados foram:',end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')

Resultado:

Os valores sorteados foram:4 2 9 1 2 
O maior valor sorteado foi: 9
O menor valor sorteado foi: 1


