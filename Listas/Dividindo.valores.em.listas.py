### --- Dividindo valores em listas ---- ###

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares
#e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

num = list()
while True:  #  vários valores - looping infinito -
        num.append(int(input('Digite um número: '))) # 'append - adicionar elementos'
        resp = input('Quer continuar? [S/N]')
        if resp in 'Nn':
            break
print(num)

## Segunda parte: Gerar listas separadas ##
# criar vetores pares e ímpares  como listas
impares = list()
pares = list()
for i,v in enumerate(num):   # 'i' = como índice e 'v = como valor' #
    if v % 2 == 0:          # se o valor da divisão for de resto 0 é par
        pares.append(v)
    elif v % 2 == 1:        # Se o valor da divisão for resto 1 (sobra) é ímpar ##
        impares.append(v)
print('+'*30)
print(f' A lista completa é: {num}.')
print(f' A lista de pares é: {pares}.')
print(f' A lista de ímpares é: {impares}.')

        

