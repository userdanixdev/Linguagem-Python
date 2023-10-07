#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#versão 02 : Com palavras diferentes

palavras=('pastel','sabonete','panela','piada','pernambuco','cachorro',
          'tabuada','paraguai','esquecido')
vogais=('a','e','i','o','u')
for c in range(0,len(palavras)):
    print(f'Na palavra "{palavras[c].upper()}", encontramos as vogais:',end="")
    for v in range(0,len(vogais)):
          if vogais[v] in palavras[c]:
              print(end=f'{vogais[v].upper()}')
          print('')
