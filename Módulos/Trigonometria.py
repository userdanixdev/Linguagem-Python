#Faça um programa que leia um ângulo qualquer e mostre na tela o valor:
#    do seno, cosseno e tangente desse ângulo.

#Lembrete: Em trigonometria existe o círculo trinogométrico a qual o:
# Eixo vertical é: SENOS
# Eixo horizontal é: COSSENOS
# A tangente é o trajeto que irá passar antre os pontos SENOS e COSSENOS.
# Os ângulos em graus centigrados no círculo trigonometrico é medido em RADIANOS.


import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO em RADIANO de {}.'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO em RADIANO de {}.'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {}.'.format(angulo, tangente))

Results:

Digite o ângulo que você deseja: 30
O ângulo de 30.0 tem o SENO em RADIANO de 0.49999999999999994.
O ângulo de 30.0 tem o COSSENO em RADIANO de 0.8660254037844387.
O ângulo de 30.0 tem a TANGENTE de 0.5773502691896257.
================================================================================================
Exemplo 02  com a nova sintaxe, 'f-string':

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO em RADIANO de {seno}.')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO em RADIANO de {cosseno}.')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente}.')

Resultado será o mesmo.
================================================================================================================

Exemplo 03 com os módulos importados da biblioteca 'math' logo abaixo:

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO em RADIANO de {seno}.')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO em RADIANO de {cosseno}.')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente}.')

** Sendo assim, o bloco fica menor, ocupa menos espaço na memória e facilita na visualização.
** Obs: o resultado será o mesmo.
======================================================================================================================================










               
