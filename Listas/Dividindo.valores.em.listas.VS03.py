### --- Dividindo valores em listas ---- ###

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares
#e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

# VERSÃO 03 - #

l=[]
l1=[]
l2=[]  # par
while True:
    lista=int(input('Digite o número: '))
    l.append(lista)    
    if lista % 2 == 0:
        l2.append(lista)
    else:
        l1.append(lista)
    r=input('Quer continuar? [S/N]').strip()[0].upper()
    while r not in 'SN':
        r=input('Opção inválida. Deseja continuar?[S/N]').strip()[0].upper()
    if r == 'N':
        break
print(f'Essa é a lista de números pares: {l2}\nEssa é a lista de números Impares:{l1}.\nA lista completa é esta:{l}')

Results:

Digite o número: 20
Quer continuar? [S/N]s
Digite o número: 21
Quer continuar? [S/N]s
Digite o número: 22
Quer continuar? [S/N]s
Digite o número: 23
Quer continuar? [S/N]s
Digite o número: 24
Quer continuar? [S/N]s
Digite o número: 25
Quer continuar? [S/N]n
Essa é a lista de números pares: [20, 22, 24]
Essa é a lista de números Impares:[21, 23, 25].
A lista completa é esta:[20, 21, 22, 23, 24, 25]
==============================================================



