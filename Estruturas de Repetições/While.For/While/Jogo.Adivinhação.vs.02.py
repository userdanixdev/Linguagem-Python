'''O computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

import random
from time import sleep
tentos=1
aleatorio=random.randrange(0,7)
print('''
Bem vindo ao jogo da adivinhação, vou pensar em um número entre 0 e 6.
Tente adivinhar.''')
num=int(input('Em que número pensei? '))
sleep(1)
print('Processando...')
sleep(2)
while aleatorio != num:
    if aleatorio > num:
        num =int(input('Maior... tente outra vez: '))
        tentos = tentos + 1
        sleep(1)
        print('Processando...')
        sleep(1)
    elif aleatorio<num:
        num=int(input('Menos... tente outra vez: '))
        tentos = tentos + 1
        print('Processando...')
        sleep(1)
    
print(f'Parabéns. Você acertou com {tentos} tentativas.')

Result:
Bem vindo ao jogo da adivinhação, vou pensar em um número entre 0 e 6.
Tente adivinhar.
Em que número pensei? 6
Processando...
Parabéns. Você acertou com 1 tentativas.
============================================================


