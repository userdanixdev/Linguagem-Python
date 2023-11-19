#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num=[[],[]]   # Declaro uma lista dentro de duas listas internas, a 1° é par.
valor = 0
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
print('*'*40)

Resultado no terminal/console:

Digite o 1° valor: 1               
Digite o 2° valor: 2
Digite o 3° valor: 3
Digite o 4° valor: 4
Digite o 5° valor: 5
Digite o 6° valor: 6
Digite o 7° valor: 7
++++++++++++++++++++++++++++++++++++++++++++++++++
Todos os valores: [[2, 4, 6], [1, 3, 5, 7]].
==================================================
Os valores ímpares digitados foram:[1, 3, 5, 7]
 e os pares:[2, 4, 6].

==============================================================

