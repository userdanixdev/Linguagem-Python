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

Resultado:
Na palavra "PASTEL", encontramos as vogais:A
E



Na palavra "SABONETE", encontramos as vogais:A
E

O

Na palavra "PANELA", encontramos as vogais:A
E



Na palavra "PIADA", encontramos as vogais:A

I


Na palavra "PERNAMBUCO", encontramos as vogais:A
E

O
U
Na palavra "CACHORRO", encontramos as vogais:A


O

Na palavra "TABUADA", encontramos as vogais:A



U
Na palavra "PARAGUAI", encontramos as vogais:A

I

U
Na palavra "ESQUECIDO", encontramos as vogais:
E
I
O
