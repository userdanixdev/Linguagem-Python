#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#versão 03 : 

palavras=('aprender','programar','linguagem','python','curso','gratis',
          'estudar','praticar','trabalhar','mercado','programador','futuro')
vogais=('a','e','i','o','u')

# uso do for para as palavras da tupla
for c in range(0,len(palavras)):
    print(f'\nNa palavra "{palavras[c].upper()}", temos:',end='')
# uso do for para cada letra           
    for v in range(0,len(vogais)):
          for x in range(0,len(vogais)):
           if vogais[x] in palavras[c][v]:
              print(vogais[x],end='')
