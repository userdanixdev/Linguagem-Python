#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor
#e o maior valor que estão na tupla.

#versão 05: Com sample (amostra aleatória) e sorted(sorteio)

from random import sample
valores = (sample(range(0, 10), 5))
valores_ordem = sorted(valores)
print(f'Os números sorteados foram {valores}')
print(f'O maior valor é {valores_ordem[-1]}')
print(f'O menor valor é {valores_ordem[0]}')
