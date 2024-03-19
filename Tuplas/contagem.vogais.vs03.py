#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Versão 03:
words=('aprender','programar','linguagem','python','curso',
          'gratis','estudar','praticar','trabalhar','mercado',
          'programador','futuro')
vogals=('a','e','i','o','u')

for w in words:
    print(f'\n Na palavra {w.upper()} temos as vogais: ', end='')
    for v in vogals:
        if v in w:
            print(f'{v.upper()}',end=' ')
            
