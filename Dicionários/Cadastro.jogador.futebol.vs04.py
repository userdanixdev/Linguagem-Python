#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 04:

jogador={}
jogador['Nome']=input('Nome:')
jogador['Partidas']=int(input('Qtd de partidas: '))
gols=list()
for i in range(jogador['Partidas']):
    print(f'Quantos gols na partida {i+1}? ')
    n_gols=int(input())
    gols.append(n_gols)
    jogador['gols']=gols
    jogador['Total']=sum(gols)
print('+'*30)
print(jogador)
print('+'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('+'*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for k,v in enumerate(gols):
    print(f'Na partida {k+1}, fez {v}')
print(f'Foi um total de {jogador["Total"]} gols.')

