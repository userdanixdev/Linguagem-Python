#Faça um programa que tenha uma função chamada ficha(), que receba dois 
#parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

# Version 02:
    
def ficha(nome=0,gols=0):
    nome=input('Nome:')
    gols = input('Gols:')    
    if nome ==0 or nome == '':
        nome = 'DESCONHECIDO'
    if gols.isnumeric():
            gols=int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')            

ficha()    