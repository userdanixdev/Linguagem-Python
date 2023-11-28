# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#Versão 02: Usando função 'sample' do random.

import random
for x in range(int(input('Número de jogos: '))):
    print(f'Jogo {x+1}: {random.sample(range(1,60),6)}')
