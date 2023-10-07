#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras=('aprender','programar','linguagem','python','curso',
          'gratis','estudar','praticar','trabalhar','mercado',
          'programador','futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

Resultado:
Na palavra APRENDER temos a e e 
Na palavra PROGRAMAR temos o a a 
Na palavra LINGUAGEM temos i u a e 
Na palavra PYTHON temos o 
Na palavra CURSO temos u o 
Na palavra GRATIS temos a i 
Na palavra ESTUDAR temos e u a 
Na palavra PRATICAR temos a i a 
Na palavra TRABALHAR temos a a a 
Na palavra MERCADO temos e a o 
Na palavra PROGRAMADOR temos o a a o 
Na palavra FUTURO temos u u o 
