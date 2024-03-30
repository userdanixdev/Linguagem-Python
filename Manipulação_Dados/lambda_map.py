# Somando 2 listas com a função Lambda:  ( função em tempo de execução )

lista_a = [1,2,3,4,5]
lista_b = [2,4,6,8,10]

list(map(lambda x,y:x+y,lista_a,lista_b))

Resultado:
[3, 6, 9, 12, 15]
=========//==============//==================//===============
# Somando os elementos de 3 listas:
a= [1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
list(map(lambda x,y,z:x+y+z, a,b,c))
Resultado:
  [15,18,21,24]
==========//===================//====================//==========
