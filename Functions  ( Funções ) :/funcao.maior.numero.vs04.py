#Faça um programa que tenha uma função chamada maior(), que receba vários
#parâmetros com valores inteiros. Seu programa tem que analisar todos os
#valores e dizer qual deles é o maior.

## Versão 04:

from time import sleep
def maior():
    #imprimelinha()
    contador = 0
    numeros = []
    while True:
        num=int(input('Digite um valor: '))
        contador += 1
        numeros.append(num)
        resposta=input('Continuar [S/N]?').strip().upper()[0]
        while resposta not in 'SN':
            resposta=input('Continuar: [S/N]?').strip().upper()[0]
        if resposta == 'N':
            break
    print('Analisando os valores informados..')
    print(f'Foram informados {contador} valores:',end=' ')
    for v in numeros:
        print(f'{v}',end=' ')
        sleep(0.3)
    print(f'\nO maior valor informado foi {max(numeros)}')        
                
#Programa principal:
maior()
