# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Lista: Pares e Ímpares
# Versão 02:

lista = []
l_pares = []
l_impares = []

for c in range(1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        l_pares.append(n)
    elif n % 2 == 1:
        l_impares.append(n)

lista.append(l_pares)
lista.append(l_impares)        

print(f'Os valores pares digitados foram: {sorted(lista[0])}\nOs impares: {sorted(lista[1])}')



