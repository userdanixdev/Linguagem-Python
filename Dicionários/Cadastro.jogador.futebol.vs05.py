#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 05:

from time import sleep
print(f'{'='*30}\n{'RENDIMENTO DO JOGADOR':^30}\n{'='*30}')
jogador={}  # Variável jogador recebe um dicionário vazio
gol = []    # Variável gol recebe uma lista vazia
total_gols  = 0 # Variavel total_gols recebe contador numerico inteiro
jogador['Nome']=input('Digite o nome do jogador: ') # Dicionário jogador recebe chave 'nome' com o valor a ser recebido pelo usuário
jogador['Partidas']=int(input(f'Quantas partidas o {jogador["Nome"]} jogou: '))
for count in range(1,jogador['Partidas']+1): # Loop de um intervalo de 1 a quantidade de partidas que o usuário colocou no dicionario
        
        g=int(input(f'Quantos gols na {count}º partida o jogador {jogador["Nome"]} marcou: ')) # Entrada de gols por partida para variavel 'g'
        sleep(0.7)
        total_gols += g # total_gols recebe o número de gols da variável 'g'
        gol.append(g)   #  Lista gol recebe o número de gols da variável 'g' colocada pelo usuário
jogador['Gols']=gol # Dicionário jogador recebe o valor da variável 'gol' que são os números de gols para a chave 'Gols'
jogador['Total de Gols']=total_gols # Dicionario jogador recebe o valor da variável 'total_gols' para a chave 'Total de Gols'
# dados gerais do jogador:
sleep(0.5)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for p in range(1,jogador['Partidas']+1):  # 'p' é o numero de partidas dentro do dicionario 'Partidas'
    sleep(0.5)
    print(f'Na {p}º partida ele marcou {jogador["Gols"][p-1]} gols.')
sleep(0.5)
print(f'Totalizando em {total_gols} gols.')    
        

