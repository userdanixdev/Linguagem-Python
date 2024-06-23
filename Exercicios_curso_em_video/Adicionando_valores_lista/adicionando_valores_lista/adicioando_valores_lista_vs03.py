# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Lista ordenada: Sem uso do sort
# Versão 03:

lista = []
for numero in range(5):
    numero = int(input('Digite um número: '))
    c = 0
    while c < len(lista) and numero > lista[c]:
        c += 1
    lista.insert(c,numero)
    print('Item adicionado',f'na posição {c}'if c < len(lista)-1 else 'no final','da lista')
print(f'\nLista ordenada: {lista}')    
    
