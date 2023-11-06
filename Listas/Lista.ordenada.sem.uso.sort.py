#Crie um programa onde o usuário possa digitar cinco valores numéricos e
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
#No final, mostre a lista ordenada na tela.

lista=list()
# temos que ler 5 valores , então é for range #
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)   # será o primeiro valor
    elif n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
             lista.insert(pos,n)
             print(f'Adicionado na posição {pos} da lista...')
            break
            pos = pos + 1
print(f'Os valores digitados em ordem foram: {lista}')      

Results:

Digite um valor: 15
Digite um valor: 20
Adicionado ao final da lista...
Digite um valor: 13
Adicionado na posição 0 da lista...
Digite um valor: 55
Adicionado ao final da lista...
Digite um valor: 36
Os valores digitados em ordem foram: [13, 15, 20, 55]

=======================================================





