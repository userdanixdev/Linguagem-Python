#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 05:

jogador={}
gol=[]
totgols=0
jogador['Nome']=input('Digite o nome do jogador: ')
jogador['Partidas']=int(input(f'Digite quantas partidas o jogador {jogador["Nome"]} jogou: '))
for count in range(1,jogador['Partidas']+1):
    g=int(input(f'Quantos gols na {count}° partida o jogador {jogador["Nome"]} marcou: '))
    totgols += g
    gol.append(g)
jogador['Gols']=gol
jogador['Total de Gols']=totgols
print('='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for p in range(1,jogador['Partidas'] +1):
    print(f' => Na {p}° partida ele marcou {jogador["Gols"][p-1]} gols.')
print(f'Totalizando em {totgols} gols.')
print('+'*30)
                       
