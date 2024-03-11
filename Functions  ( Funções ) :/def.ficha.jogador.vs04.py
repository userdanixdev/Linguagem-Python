#Faça um programa que tenha uma função chamada ficha(), que receba dois 
#parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

# Version 04:
    
def dados(jogador,gol):
    if jogador == '':
        jogador = 'DESCONHECIDO'
    if gol == '':
        gol = 0
    return f'O jogador {jogador} fez {gol} gols no campeonato'
nome=input('Nome do Jogador: ').upper()
gols=input(f'Quantos gols {nome} fez:')
print(dados(nome,gols))        
