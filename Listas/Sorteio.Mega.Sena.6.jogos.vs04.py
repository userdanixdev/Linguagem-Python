# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#Versão 04:

from random import sample
lista = list(range(1,61))
quantidade = int(input('Quer gerar quantos jogos? '))
for x in range(1,quantidade+1):
    bilhete = sample(lista,6)
    print(f'Jogo {x}:{sorted(bilhete)}')
print('Boa sorte.')    



#Neoenergia
#Protocolo: 63787143
#34659318 - Zap
