#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Para isso devemos importar a biblioteca 'MATH' e acionar a função 'TRUNC'#
# A função 'trunc' é um método para tirar a porção inteira. ##
# 'trunc' é 'TRUNCATE' - irá cortar a parte do número) ##
==================================================================

Exemplo 01 :

import math 
numero = float(input('Digite um número Real qualquer para mostrar sua porção inteira: '))
print('O valor digitado foi {} e sua porção intera é: {}'.format(numero,math.trunc(numero)))

Resultado:

Digite um número Real qualquer para mostrar sua porção inteira: 3.1415
O valor digitado foi 3.1415 e sua porção intera é: 3
=====================================================================================================
Exemplo 02:

from math import trunc    #Nesse caso, especifiquei da biblioteca 'math' o método 'trunc'#
numero = float(input('Digite um número real qualquer para mostrar sua porção inteira: '))
print('O valor digitado foi {} e sua porção inteira é: {}'.format(numero,trunc(numero)))

Results:

Digite um número real qualquer para mostrar sua porção inteira: 3.1415
O valor digitado foi 3.1415 e sua porção inteira é: 3

*** ATENÇÃO: Obtivemos o mesmo resultado. ****
============================================================================================================

Exemplificações aplicadas na nova sintaxe 'f-strings':

Exemplo01:

import math
numero=float(input('Digite um número real qualquer para mostrar sua porção inteira: '))
print(f'O valor digitado foi {numero} e sua porção inteira é:{math.trunc(numero)}')

Exemplo02:  #com importação de trunc diretamente da biblioteca 'math'

from math import trunc
numero=float(input('Digite um número real qualquer para mostrar sua porção inteira: '))
print(f'O valor digitado foi {numero} e sua porção inteira é:{trunc(numero)}')

=====================================================================================================
