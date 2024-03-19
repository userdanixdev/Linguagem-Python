#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Versão 02:
palavras=('aprender','programar','linguagem','python','curso',
          'gratis','estudar','praticar','trabalhar','mercado',
          'programador','futuro')
vogais=('a','e','i','o','u')

for c in range(0,len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()}, encontramos as vogais: ',end='')
    for v in range(0,len(vogais)):
        if vogais[v] in palavras[c]:
            print(f'{vogais[v].upper()}.',end='')
