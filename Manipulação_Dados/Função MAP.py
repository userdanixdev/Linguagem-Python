# Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento:
lista=[1,2,3]
ao_cubo = [item**3 for item in lista]
print(ao cubo)
Resultado:
[1,8,27]
=================//================================
def potencia(x):
  resultado=[]
  for item in x:
    resultado.append(item**3)
  return resultado
lista = [1,2,3]
print('Lista Original',lista)
print('Terceira potência de cada elementos:', potencia(lista))
=================//=====================//========================//
## Utilizando o método MAP:
def potencia(x):
  returnX**3
numeros=[1,2,3]
numeros_ao_cubo=list(map(potencia,numeros))
print(numeros_ao_cubo)
=====================//==========================//============



