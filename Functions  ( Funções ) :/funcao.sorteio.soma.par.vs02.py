#Faça um programa que tenha uma lista chamada números e duas funções chamadas
#sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
#colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
#os valores pares sorteados pela função anterior.


## Versão 02:

from random import randint
from time import sleep

def sortear(n1,n2,n3,n4,n5):
    numeros = [n1,n2,n3,n4,n5]
    print(f'Sorteando 5 valores da lista: ',end='')
    for numero in numeros:
        print(numero,end=' ')
        sleep(0.3)
    print('Pronto.')

    def soma_par():
        pares = 0
        for i in numeros:
            if i % 2 == 0:
                pares += i
        print(f'Somando os valores pares de {numeros} temos {pares} pares.')
    soma_par()

# Main Program:
sortear(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
                        

