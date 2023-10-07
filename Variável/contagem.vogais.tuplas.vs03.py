#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#versão 03 : 

palavras=('aprender','programar','linguagem','python','curso','gratis',
          'estudar','praticar','trabalhar','mercado','programador','futuro')
vogais=('a','e','i','o','u')

# uso do for para as palavras da tupla
for c in range(0,len(palavras)):
    print(f'\nNa palavra "{palavras[c].upper()}", temos:',end='') # interessante colocar o contra barra n para formatação
# uso do for para cada letra           
    for v in range(0,len(vogais)):
          for x in range(0,len(vogais)):
           if vogais[x] in palavras[c][v]:
              print(vogais[x],end='')

Resultado:
Na palavra "APRENDER", temos:ae
Na palavra "PROGRAMAR", temos:o
Na palavra "LINGUAGEM", temos:iu
Na palavra "PYTHON", temos:o
Na palavra "CURSO", temos:uo
Na palavra "GRATIS", temos:ai
Na palavra "ESTUDAR", temos:eu
Na palavra "PRATICAR", temos:ai
Na palavra "TRABALHAR", temos:aa
Na palavra "MERCADO", temos:ea
Na palavra "PROGRAMADOR", temos:o
Na palavra "FUTURO", temos:uu
