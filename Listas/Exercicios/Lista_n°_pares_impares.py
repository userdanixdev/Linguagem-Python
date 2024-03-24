#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num=[[],[]]   # Declarar uma lista dentro de duas listas internas, o 1°é PAR.
valor = 0
# Ordenação da lista com o sort()
num[0].sort()
num[1].sort()
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('+'*50)
print(f'Todos os valores: {num}.')
print('='*50)
print(f'Os valores ímpares digitados foram:{num[1]}\n e os pares:{num[0]}.')
print('='*50)

