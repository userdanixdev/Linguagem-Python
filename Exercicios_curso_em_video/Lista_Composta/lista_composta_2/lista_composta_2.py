# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Lista: Pares e Ímpares
# Versão 01:

lista = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor) # Para valores pares
    else:
        lista[1].append(valor) # Para valores impares
print('='*30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são: {lista[0]}\nOs valores impares: {lista[1]}')
