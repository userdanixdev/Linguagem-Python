#Faça um programa que tenha uma função chamada maior(), que receba vários
#parâmetros com valores inteiros. Seu programa tem que analisar todos os
#valores e dizer qual deles é o maior.

## Versão 06:
## Incremento de outra função de seperação:
def linha():
    print('+'*30)
    
def maior(*num):
    from time import sleep
    linha()
    i=0
    print('Analisando os valores passados...')
    for n in num:
       sleep(0.3)
       print(f'{n}',end=' ')
       i += 1
    print(f'Foram informados {i} valores.')
    linha()
    if len(num)==0:
        print(f'O maior valor informado foi 0.')
           
    else:        
        print(f'O maior valor encontrado foi {max(num)}.')

maior(0)
maior(1,3,6,15,10,12)
