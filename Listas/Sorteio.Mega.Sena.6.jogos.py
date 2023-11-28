# Sorteio da Mega Sena

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Lista composta:

# Guardar muitos dados separados por sessão:

# Gerador número aleatórios: 1°passo
#Necessário quanto o usuário desejar... Pelo menos 6 vezes, de acordo com enunciado:
#Fazer n vezes:
from random import randint
from time import sleep
quant = int(input('Quantos jogos vc quer que eu sorteie? ')) # Perguntar ao usuário quantas jogos ele vai querer fazer
total_jogos = 1   # Colocar uma variável de total de vezes que ele vai sortear.
jogos = list()   # Toda vez que houver o sorteio, escolhido pelo usuário, irá ficar dentro de outra lista.         
contador = 0
lista=list()
while total_jogos <= quant:
    contador=0
    while True:
        num = randint(1,60)
        if num not in lista:        # Se o número não estiver na lista, adicionar com o método append
            lista.append(num)  
            contador += 1
        if contador >= 6:
            break
    lista.sort()    # Ordenar a lista de forma crescente para marcação no papel.
    jogos.append(lista[:])   # Cópia da lista [:]
    lista.clear()  # Limpa a lista depois
    total_jogos += 1
print(f' Você sorteou {quant} jogos. Os números sorteados foram: {jogos}.')
print('Com a formatação adequada usando o método ''enumarate')
# Mudança na resposta:
# for para cada elemento da lista de jogos:
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}.')  ## PARA RETIRAR O 'ZERO' COLOCAR 'i'+1
                              #Com incremento '"+1"' para retirar o jogo 0.')
    sleep(1)
print('BOA SORTE!')
    





























