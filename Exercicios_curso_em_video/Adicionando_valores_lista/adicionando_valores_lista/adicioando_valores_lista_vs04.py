# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Lista ordenada: Sem uso do sort
# Versão 04:

lista = []
for c in range(1,6):
    numero = int(input(f'Digite o {c}º número: '))
    if c == 1 or numero >= lista[-1]:
        lista.append(numero)
    elif numero <= lista[0]:
        lista.insert(0,numero)
    elif lista[0] <= numero <= lista[1]:
        lista.insert(1,numero)
    elif lista[1] <= numero <= lista[2]:
        lista.insert(2,numero)
    elif lista[2] <= numero <= lista[3]:
        lista.insert(3,numero)
print(lista)        
