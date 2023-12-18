#Faça um programa que tenha uma função chamada contador(),
#que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

#Versão 02:
from time import sleep

def contador():
    print('Contagem de 1 até 10 de 1 em 1:')
    for c in range(1,11):
        print(c, end= ' ')
        sleep(0.7)
    print('\nContagem de 10 até 0 de 2 em 2: ')
    for c in range(10,-1,-2):
        print(c, end= ' ')
        sleep(0.2)
    print('\nAgora sua vez: ')
    inicio=int(input('Inicio: '))
    fim=int(input(' FIm: '))
    passo = int(input('Passo: '))
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} indo de {passo} em {passo}: ')
    if inicio < fim:
        for c in range(inicio,fim+1,passo):
            print(c,end=' ')
            sleep(0.2)
    elif inicio > fim:
        if passo > 0:
            for c in range(inicio,fim -1, passo):
                print(c,end=' ')
                sleep(0.2)
    if inicio == fim:
        print('Não existe contagem.')
    print()
    print('Fim do programa')
contador()    
    
