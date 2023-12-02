#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 02:

jogador=dict()
jogador['Nome']=str(input('Nome do Jogador: '))
jogador['Partidas']=int(input('Quantas partidas jogou: '))
jogador['Gols']=list()
for i in range(0,jogador['Partidas']):
               jogador['Gols'].append(int(input(f'Quantos gols na partida{i+1}? ')))
jogador['Total']=sum(jogador['Gols'])
print('+'*30)
print(jogador)
print('+'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('+'*30)
print(f'O jogador {jogador["Nome"]} tem {jogador["Partidas"]} partidas.')
for c in range(0,jogador['Partidas']):               
    print(f'=> Na partida {c+1} fez {jogador["Gols"][c]}.')
print(f'E fez um total de {jogador["Total"]} gols.')               
