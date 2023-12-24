#Faça um programa que tenha uma lista chamada números e duas funções chamadas
#sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
#colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
#os valores pares sorteados pela função anterior.


## Versão 04:

from random import randint

def sorteia(n):
        "Retorna uma lista com n valores aleatórios entre 1 a 10."
        return [randint(1,10) for i in range(n)]

def par(x):
        "Retorna True se x for par, False caso contrário."
        return x % 2 == 0

def soma_par(valores):
        "Retorna a soma dos valores pares."
        return sum([v for v in valores if par(v)])

print('Sorteando 5 valores da lista: ',end=' ')
valores = sorteia(5)
for v in valores: print(f'{v}', end= ' ')
print('Pronto.')
print(f'Somando os valores pares de {valores}, temos {soma_par(valores)}')
