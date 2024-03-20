#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
#Também indique o menor e o maior valor que estão na tupla.

'''Como irei randomizar valores e colocar em uma tupla?'''

# versão 4:

from random import sample

valores=(sample(range(0,10),5))
valores_ordem = sorted(valores)
print(f' Os números sorteados foram: {valores}.')
print(f' O maior valor é: {valores_ordem[-1]}')
print(f'O menor valor é {valores_ordem[0]}')

