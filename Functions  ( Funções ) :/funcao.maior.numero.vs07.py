#Faça um programa que tenha uma função chamada maior(), que receba vários
#parâmetros com valores inteiros. Seu programa tem que analisar todos os
#valores e dizer qual deles é o maior.

## Versão 07:

def linha():
    print('+'*30)
    
def maior():
    lista=list()
    while True:
        num = int(input('Digite um valor: '))
        linha()
        lista.insert(0,num)
        if num == 0:
            lista.pop(0)
            break
    print(f'Os valores digitados foram:\n{lista}')
    print(f'O maior valor foi: {max(lista)}')

    
maior()

