# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#Versão 06:

import random
lista_jogo=list()
qnt_jogo=int(input('Quantos jogos quer que eu sorteie? '))
for c in range(1,qnt_jogo+1):
    print(f'Jogo{c}:',end='')
    palpite=random.sample(range(60),6)
    lista_jogo.append(palpite)
    print(sorted(lista_jogo[0]))
    lista_jogo.clear()
print('Boa sorte.')    


#Neoenergia
#Protocolo: 63787143
#34659318 - Zap
