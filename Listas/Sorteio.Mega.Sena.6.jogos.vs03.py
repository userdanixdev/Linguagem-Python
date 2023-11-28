# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#Versão 03:

from time import sleep
from random import randint
jogo = list()
quantidade = int(input('Quer gerar quantos jogos? '))
for x in range(0,quantidade):
    while len(jogo)<6:
        n=randint(1,60)
        if n not in jogo:
            jogo.append(n)
    print(f'Jogo{x+1}:{sorted(jogo)}')
    sleep(.5)
    jogo.clear()
print('Boa sorte.')    



#Neoenergia
#Protocolo: 63787143
#34659318 - Zap
