#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 03:
from time import sleep
# Declarando as variáveis:
jogador= dict() # Jogador recebe um dicionário declarado.
gol = []   # Gol recebe lista
partidas = 0 # Partida como contador
total_gols = 0 # Total_ gols contador também

# Inserindo dados pelo usuário:
print(f'{'+'*50}\n{'Rendimento do jogador':^48}\n{'+'*50}\nInsira os dados abaixo...')
sleep(0.5)
jogador['Nome']=input('Nome do jogador: ')
sleep(0.3)
partidas=int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

# Inserir um laço para cada partida, computar os gols:
for p in range(partidas): # para cada partida, a variável 'gol' recebe os gols da partida.
    gol.append(int(input(f'Quantos gols da partida {p+1}? ')))
    total_gols += gol[p] # O contador total_gols recebe os gols
jogador['Gols']=gol.copy() # O dicionário jogador com a chave 'gols' recebe uma cópia dos gols recebidos
jogador['Total']=total_gols # Dicionário jogador com chave 'total' irá receber a variável contadora total_gols

# Mostrar valores na tela:
sleep(0.5)
print(f'{'+'*50}\n{'Rendimento do jogador:':^48}\n{'+'*50}')
sleep(0.5)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
sleep(0.5)
for p in range(len(jogador["Gols"])):
    sleep(0.7)
    print(f' Na partida {p+1}, fez {jogador["Gols"][p]} gols.')
# Fora do laço:
sleep(0.8)
print(f'Foi um total de {total_gols} gols.')
sleep(0.8)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')

# Mostrar os valores no dicionário:
sleep(1)
print(f'{'+'*50}\n{'Percorrendo o dicionário JOGADOR':^48}\n{'+'*50}')
sleep(1)
print(jogador)
sleep(1)
print('='*50)
for k,v in jogador.items(): # A função items percorre o indice e valor juntamente com o laço 'for':
    sleep(1)
    print(f'O campo {k} tem o valor {v}.')
print('+'*50)
