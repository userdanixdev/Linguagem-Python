# Jogo de Dados:
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem,
#sabendo que o vencedor tirou o maior número no dado.


# Versão 02:

from random import randint
from operator import itemgetter

numeros={}   # Dicionário vazio
for i in range(4):    #Laço para 4 jogadores
# Abaixo, a sintaxe colocará no dicionário vazio 'numeros' um número aleatório entre 1 e 6 para cada jogador.
    numeros[f'jogador_{i+1}']=randint(1,6)
#Parte 02:
# Mostra, abaixo, os números que foram sorteados de cada um na ordem de inserção no dicionário:
print('Valores sorteados: ')
for k, v in numeros.items():
    print(f'O{k} tirou {v}.')
#Parte 03:
# Para mostrar o vencedor do jogo do maior para o menor:
print('Ranking dos jogadores: ')
for i,v in enumerate(sorted(numeros.items(),key=itemgetter(1),reverse=True)):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
