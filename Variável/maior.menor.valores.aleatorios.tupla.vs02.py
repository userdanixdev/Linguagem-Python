#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
#Também indique o menor e o maior valor que estão na tupla.

#Versão 02

from random import sample # Espaço amostral função matemática aleatória
a = tuple(sample(range(10),5))
print(f'{a},\n O maior valor é {max(a)}\n e o menor é {min(a)}.')
