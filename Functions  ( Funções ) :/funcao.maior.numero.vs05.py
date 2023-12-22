#Faça um programa que tenha uma função chamada maior(), que receba vários
#parâmetros com valores inteiros. Seu programa tem que analisar todos os
#valores e dizer qual deles é o maior.

## Versão 05:


from time import sleep

def maior(*num):
    print('+'*25)
    print('Analisando os valores passados...')
    for c in range(0,len(num)):
        print(num[c], end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor encontrado foi {max(num)}.')

maior(0)
maior(1,3,6,15,10,12)
