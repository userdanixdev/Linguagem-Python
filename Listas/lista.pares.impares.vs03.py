#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#Versão 03:

num=[[],[]]
for c in range(7):
    n=int(input(f'Digite o {c+1}° número: '))
    num[0].append(n) if n % 2 == 0 else num[1].append(n)
print('+'*22,f'\nNúmeros pares digitados:{sorted(num[0])}\nNúmero ímpares digitados:{sorted(num[1])}.')    

Resultado no console/terminal:

Digite o 1° número: 1   
Digite o 2° número: 2
Digite o 3° número: 3
Digite o 4° número: 4
Digite o 5° número: 5
Digite o 6° número: 6
Digite o 7° número: 7
++++++++++++++++++++++ 
Números pares digitados:[2, 4, 6]
Número ímpares digitados:[1, 3, 5, 7].
