#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


#Versão 04:

from time import sleep
print(f'{'='*30}\n{"Rendimento do jogador":^30}\n{'='*30}\n{'Insira os dados abaixo:'}')
sleep(0.7)
jogador={}# variável jogador recebe um dicionário
jogador['Nome']=input('Nome: ') # Usuário deve colocar o nome do jogador
sleep(0.5)
jogador['Partidas']=int(input('Quantidade de partidas: ')) # Usuário deve colocar o número de partidas
gols=list()
# Colocar o número de gols pelo usuário dentro das partidas:
for i in range(jogador['Partidas']):
    print(f'Quantos gols na partida {i+1}? ')
    sleep(0.5)
    n_gols=int(input()) #<- Número de gols é a variável que o usuário irá colocar
    gols.append(n_gols) # O número de gols será colocado na variável lista gols.
    jogador['Gols']=gols # Cria-se a chave 'Gols' e coloca a variável lista gols com o n_gols
    jogador['Total']=sum(gols) # Chave 'Total' do dicionário jogador recebe a soma da variável lista gols com os gols computados pelo usuário]
media_gols = jogador['Total']/jogador['Partidas'] # calculo para média de gols por partida
# Inserir a chave 'Média por partida' dentro do dicionário
jogador['Média']=media_gols
# Dados gerais do dicionário jogador :
sleep(2)
print(f'{'+'*30}\n{"Dados do dicionário jogador":^30}\n{'+'*30}\n{jogador}')
sleep(3)
print(f'{'+'*30}\n{"Varredura do dicionário jogador":^30}\n{'+'*30}')
for k,v in jogador.items():
    sleep(0.7)
    print(f'O campo {k} tem o valor {v}.')
    sleep(0.7)
print(f'{'+'*30}\n{"Quantas partidas":^30}\n{"QTD GOLS":^30}\n{'+'*30}')
sleep(3)
# Dados gerais do jogador:
for k, v in enumerate(gols):
    sleep(0.7)
    print(f'Na partida {k+1}, fez {v} gols') # Sendo k a chave com o nome de 'gols' e o valor do dicionário como 'v'
sleep(0.5)    
print(f'Total de {jogador["Total"]} gols.')
print(f'Média de gols por partida: {media_gols:.2f}')

