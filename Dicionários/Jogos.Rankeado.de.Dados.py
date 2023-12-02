# Jogo de Dados:
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem,
#sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
jogo={'jogador1':  randint(1,6),
      'jogador2': randint(1,6),
      'jogador3': randint(1,6),
      'jogador4': randint(1,6)}
ranking=list()
print('Valores sorteados:')
for keys, values in jogo.items():
    print(f'{keys} tirou {values} no dado.')
# para colocar em ordem temos que criar outro dicionário vazio:
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('ranking dos jogadores:') #
for indice, valor in enumerate(ranking):
        print(f'{indice+1}º lugar: {valor[0]} com {valor[1]}')                                       
