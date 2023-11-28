# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#Versão 05:

from random import randint
mega=[]
temp=[]
qnt=int(input('Quantos jogos deseja? '))

for i in range(1,qnt+1):
    for n6 in range(1,7):
        temp.append(randint(1,60))
    mega.append(temp[:])
    temp.clear()
for i in mega:
    print(i)


#Neoenergia
#Protocolo: 63787143
#34659318 - Zap
