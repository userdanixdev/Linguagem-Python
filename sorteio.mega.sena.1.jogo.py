# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Lista composta:

# Guardar muitos dados separados por sessão:

# Gerador número aleatórios: 1°passo
from random import randint
contador = 0
lista=list()
while True:
    num = randint(1,60)
    if num not in lista:        # Se o número não estiver na lista, adicionar com o método append
        lista.append(num)  
        contador += 1
    if contador >= 6:
        break
lista.sort()    # Ordenar a lista de forma crescente para marcação no papel.
print(f'Os números sorteados foram: {lista}.')
