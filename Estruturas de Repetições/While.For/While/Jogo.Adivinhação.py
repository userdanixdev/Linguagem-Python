'''O computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
maquina=randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10...')
print('Será que vc consegue adivinhar qual é? ')
acertou=False
palpites=0 #contagem de palpites que precisou para acertar
while not acertou:
    jogador=int(input('Qual é seu palpite? '))
    palpites = palpites + 1
    if jogador == maquina:
        acertou=True
    else:                    # facilitador
        if jogador<maquina:
            print('Maior...tente mais uma vez.')
        elif jogador >maquina:
             print('Menos... Tente mais uma vez...')
print(f'Acertou com {palpites} tentativas. Parabéns!')      

Resultado:

Sou seu computador... Acabei de pensar em um número entre 0 e 10...
Será que vc consegue adivinhar qual é? 
Qual é seu palpite? 4
Menos... Tente mais uma vez...
Qual é seu palpite? 1
Menos... Tente mais uma vez...
Qual é seu palpite? 2
Menos... Tente mais uma vez...
Qual é seu palpite? 3
Menos... Tente mais uma vez...
Qual é seu palpite? 0
Acertou com 5 tentativas. Parabéns!
===============================================================



