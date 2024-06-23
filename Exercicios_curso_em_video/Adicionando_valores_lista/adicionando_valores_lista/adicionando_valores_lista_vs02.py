# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Lista ordenada: Sem uso do sort
# Versão 02:

lista = list()
for c in range(0,5):
    n = int(input('Digite o número: '))
    if c == 0 or n > lista[-1]:  # Ou se for n for maior que o menor da lista
        lista.append(n)
    else:
        for posicao,x in enumerate(lista):
            if n <= x:
                lista.insert(posicao,n)
                break
print(lista)            

    
