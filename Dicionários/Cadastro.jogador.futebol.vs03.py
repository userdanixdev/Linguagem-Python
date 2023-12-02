#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 03:

jogador=dict()
gol=[]
partidas=totalgols = 0
jogador['Nome']=input('Nome do jogador:')
partidas=int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for p in range(partidas):
    gol.append(int(input(f' Quantos gols na partida {p+1}? ')))
    totalgols += gol[p]
jogador['Gols']=gol.copy()
jogador['Total']=totalgols
print('+'*30)
print(jogador)
print('='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('+'*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for p in range(len(jogador["Gols"])):
    print(f' == Na partida {p+1}, fez {jogador["Gols"][p]} gols.')
print(f'Foi um total de {totalgols} gols.')
print()
