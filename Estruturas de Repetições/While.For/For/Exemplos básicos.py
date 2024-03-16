# Imprimir números no intervalo de 0 a 100 contanto de 2 em 2:

for i in range(0,101,2):
  print(i, end=' ')

Resultado:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 

# Uso de Strings também podem formar sequência lógicas no looping, vejamos:

for caracter in 'Python é uma linguagem de programação!':
  print(caracter,end=' ')

Resultado:
P y t h o n   é   u m a   l i n g u a g e m   d e   p r o g r a m a ç ã o !

## Multiplicando elementos de cada lista:

lista1 = [0,1,2,3,4]
lista2 = [1.2.3]
for elemento_lista1 in lista1:
  for elemento_lista2 in lista2:
    print(elemento_lista1 * elemento_lista2, end=' ')
  print('|||', end=' ')

Resultado:

0 0 0 ||| 1 2 3 ||| 2 4 6 ||| 3 6 9 ||| 4 8 12 |||

# O elemento número 47 aparece duas vezes nas listas?

lista1 = [10,16,24,39,47]
lista2 = [32,89,47,86,12]
for elemento_lista1 in lista1:
  for elemento_lista2 in lista2:
    if elemento_lista1 == 47 and elemento_lista2 = 47
      print('O número 47 foi encontrado nas duas listas!')
    
