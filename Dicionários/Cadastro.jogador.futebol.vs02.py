#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 02:

# Ler o nome do jogador e quantas partidas ele jogou.
# Para isso vamos criar um dicionário com as chaves 'Nome','Partidas' e 'Gols' e os valores serão colocados pelo usuários
jogador=dict()
jogador['Nome']=str(input('Nome do Jogador: '))
jogador['Partidas']=int(input('Quantas partidas jogou: '))
jogador['Gols']=list()
# De acordo com o número de partidas colocadas, irá receber um laço com um input ao usuário sobre quantos gols
for i in range(0,jogador['Partidas']):
               jogador['Gols'].append(int(input(f'Quantos gols na partida{i+1}? ')))
# O dicionário Partidas recebe a soma de gols.
jogador['Total']=sum(jogador['Gols'])
print('+'*30)
print(jogador)
print('+'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('+'*30)
print(f'O jogador {jogador["Nome"]} tem {jogador["Partidas"]} partidas.')
# Mostrar o total de partidas e o total de gols:
for c in range(0,jogador['Partidas']):               
    print(f'=> Na partida {c+1} fez {jogador["Gols"][c]}.')
print(f'E fez um total de {jogador["Total"]} gols.')               

_________________________________________________________________________________________________________________
# Aproveitamento jogador de futebol
    
from time import sleep
# Ler o nome do jogador e quantas partidas ele jogou.
# Para isso vamos criar um dicionário com as chaves 'Nome','Partidas' e 'Gols' e os valores serão colocados pelo usuários
jogador=dict()
jogador['Nome']=str(input('Nome do Jogador: '))
jogador['Partidas']=int(input('Quantas partidas jogou? '))
jogador['Gols']=list()
sleep(0.5)
# De acordo com o número de partidas colocadas, irá receber um laço com um input ao usuário sobre quantos gols
for indice in range(0,jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Quantos gols na partida {indice+1}°? ')))
    sleep(0.5)    
jogador['Total']=sum(jogador['Gols'])
# O dicionário Partidas recebe a soma de gols.
sleep(0.5)
# Mostrar o total de partidas e o total de gols:
print(f'O jogador {jogador["Nome"]} tem {jogador["Partidas"]} partidas.')
for c in range(0,jogador['Partidas']):
    print(f' Na partida {c+1} fez {jogador["Gols"][c]}.')
print(f'E fez um total de {jogador["Total"]} gols.')    
