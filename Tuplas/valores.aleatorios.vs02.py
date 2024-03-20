#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
#Também indique o menor e o maior valor que estão na tupla.

'''Como irei randomizar valores e colocar em uma tupla?'''

# versão 2:

from random import sample
a= tuple(sample(range(10),5))
print(f'{a},\n O maior valor è {max(a)}\n e o menor é {min(a)}.')
