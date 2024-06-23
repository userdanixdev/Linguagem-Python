# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Lista ordenada: Sem uso do sort
# Versão 05:

lista = list()
for c in range(5):
    n = int(input('Digite um número: '))
    if c == 0 or n > max(lista):
        lista.append(n)
    else:
        for indice, valor in enumerate(lista):
            if n < valor:
                lista.insert(indice,n)
                break
    print(f'{n} inserido na posição {lista.index(n)}')
print(f'\nValores digitados em ordem: {lista}')    
