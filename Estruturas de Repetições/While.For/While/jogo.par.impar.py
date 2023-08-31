# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#Jogo par ou ímpar.

from random import randint
v=0
while True:  
    jogador=int(input('Diga um valor: '))
    computador=randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=input('Par ou Ímpar? [P/I]').strip().upper()[0]
    print(f'Vc jogou {jogador} e o PC {computador}. Total de {total}.')
    if tipo == 'P':
        if total % 2 ==0:
            print('Vc venceu.')
            v = v + 1
        else:
            print('vc perdeu.')
            break
    elif tipo == 'I':
         if total % 2 ==1:
             print('vc venceu')
             v=v+1
         else:
             print('Vc perdeu')
             break
    print('Vamos jogar novamente?')
print(f'fim do jogo. vc venceu {v} vezes.')


     
        
