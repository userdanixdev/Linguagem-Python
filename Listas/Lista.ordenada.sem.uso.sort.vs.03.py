#Crie um programa onde o usuário possa digitar cinco valores numéricos e
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
#No final, mostre a lista ordenada na tela.

#Versão 03

lista = list()
for c in range(5):
    n = int(input('Digite o número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for pos,x in enumerate(lista):
            if n <= x:
                lista.insert(pos,n)
                break
print(lista)    

Result:

Digite o número: 4
Digite o número: 6
Digite o número: 2
Digite o número: 10
Digite o número: 3
[2, 3, 4, 6, 10]
=================================================
