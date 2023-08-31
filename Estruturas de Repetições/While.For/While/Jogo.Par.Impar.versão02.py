# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#Jogo par ou ímpar. versão02 #

from random import randint
from time import sleep
print('Jogo do par ou ímpar')
print('Processando...,')
sleep(1)
par = impar = soma = cont = 0
while True:
    pc=randint(0,10)
    num=int(input('Digite um número: '))
    cont = cont +1
    par_impar=input('Vc quer par ou ímpar? ').upper().strip()[0]
    print(f'O pc escolheu {pc} e vc {num}.')
    if (pc+num)%2 == 0:
        soma=par
        if par_impar == 'Pp':
            print(f'{pc+num} é par. Vc ganhou.')
        else:
            print(f'{pc+num} é ímpar. Vc perdeu.')
            break
    elif (pc+num)%2 !=0:
         if par_impar =='iI':
             print(f'{pc+num} é ímpar. Vc ganhou.')
         else:
             print(f'{pc+num} é Ímpar. Vc perdeu.')
             break
print(f'Vc ganhou {cont} vez(es) do computador, parabéns.')           

