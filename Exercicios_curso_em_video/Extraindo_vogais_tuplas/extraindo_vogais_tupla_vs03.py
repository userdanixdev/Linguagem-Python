# Extraindo vogais de uma tupla:
# Versão 03 : Uma tupla com vogais

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar'
            'trabalhar','mercado','programador','futuro')

# tupla de vogais:
vogais = ('a','e','i','o','u')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ',end='/')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra,end='/')
