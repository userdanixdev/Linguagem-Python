#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#versão 04 :

x=('ERICK','STEFANY','JUNIOR','CIDA','ALINE')
y=('A','E','I','O','U')
for c in x:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for r in y:
        if r in c:
            print(f'{r}',end='')


