#Crie um programa onde o usuário possa digitar cinco valores numéricos e
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
#No final, mostre a lista ordenada na tela.

#Versão 02 - BEST VERSION -

lis=[]
for c in range(1,6):
    n = int(input(f'Digite o {c}° número: '))
    if c == 1 or n>lis[-1]:
        lis.append(n)
    elif n <= lis[0]:
        lis.insert(0,n)
    elif lis[0]<=n<= lis[1]:
        lis.insert(1,n)
    elif lis [1]<= n <=lis[2]:
        lis.insert(2,n)
    elif lis[2]<= n <= lis[3]:
        lis.insert(3,n)
print(lis)        

Results:

Digite o 1° número: 4
Digite o 2° número: 6
Digite o 3° número: 3
Digite o 4° número: 1
Digite o 5° número: 10
[1, 3, 4, 6, 10]

=============================================


