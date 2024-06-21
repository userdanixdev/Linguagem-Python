# Extraindo vogais de uma tupla:
# Versão 02

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar'
            'trabalhar','mercado','programador','futuro')


for p in range(0,len(palavras)):
    for c in range(0,len(palavras[p])):
               if c == 0:
                   print(f'\nNa palavra {palavras[p].upper()} temos: ',end='/')
               if palavras[p][c] in 'aeiou':
                   print(f'{palavras[p][c]}',end='/')
