#Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e  imprima a lista
def listagem(lista):
  if len(lista) ==4:
    lista.append('Novo elemento')
    lista.append('Novo elemento')
    print('lista atualizada:',lista)
minha_lista=[1,2,3,4]
listagem(minha_lista)
