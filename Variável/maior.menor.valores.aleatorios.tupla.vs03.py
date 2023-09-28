#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
#Também indique o menor e o maior valor que estão na tupla.

#Versão 04

import random
maior = menor = int
tupla=(random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
for i in range(0,5):
       if(i== 0 or tupla[i]>maior):
           maior=tupla[i]
       if(i==0 or tupla[i]<menor):
           menor=tupla[i]
print(f'{tupla}\n Maior número:{maior}\n O menor é:{menor}')       

Resultado:

(6, 5, 8, 4, 5)
 Maior número:8
 O menor é:4

