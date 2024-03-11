#Faça um programa que tenha uma função chamada ficha(), que receba dois 
#parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

# Version 03:
    
def ficha(nome, gols):
    if not nome:
        nome = 'DESCONHECIDO'
    if gols.isnumeric():
        gols = int(gols)
    else:
      gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato brasileiro'
nome=input('Nome do jogador: ').strip()
gols=input('Número de gols:')
print(ficha(nome,gols))
    
