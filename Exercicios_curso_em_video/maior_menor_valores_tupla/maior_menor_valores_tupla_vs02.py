# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
# Versão 02 : Com laço for

print('Versão 02')
a=tuple(randint(1,10) for i in range(5))
print()
print(a)
print(f'O maior valor da tupla:{max(a)}\n e o menor:{min(a)}.')
print()
print('Versão 02: Incremento de 1 a 100.')
a = tuple(i for i in range(1,101))
print()
print('Escolhe de 1 a 10 até 100.')
a = tuple(randint(1,10) for i in range(1,101))
print(a)
print('\nVersão 02: Inverso - Vai escolher de 0 a 100 com alcance de 1 a 10')
a = tuple(randint(1,100) for i in range(1,10))
print(a)
print(f'O valor máximo adquirido: {max(a)}\n e o valor mínimo adquirido: {min(a)}.')
print()







