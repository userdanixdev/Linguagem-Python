#Faça um programa que tenha uma função chamada maior(), que receba vários
#parâmetros com valores inteiros. Seu programa tem que analisar todos os
#valores e dizer qual deles é o maior.

## Versão 02:

from time import sleep

def maior(*num): 
    contador=0
    print('+'*30)
    print('Analisando os valores passados...')
    sleep(0.3)
    for c in num:
        contador += 1
        print(f'{c}', end=' ')   ### Para contar o índice dentro do laço com o sleep ##
        sleep(0.2)
    if contador > 0:
        maior = max(num)
        sleep(0.3)
    else:
        maior=0
        sleep(0.3)
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
                


#Programa principal:
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
