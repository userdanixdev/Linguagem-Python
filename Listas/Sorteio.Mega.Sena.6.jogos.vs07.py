# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#Versão 07:

from random import randint
lista=[]
quant=int(input('Digite a quantidade de jogos: '))
for jogo in range(1, quant+1):
    n1=randint(1,60)
    n2=randint(1,60)
    n3=randint(1,60)
    n4=randint(1,60)
    n5=randint(1,60)
    n6=randint(1,60)
    lista = [n1,n2,n3,n4,n5,n6]
    print(f'Jogo{jogo}:{sorted(lista)}')
