#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#Versão 03:

num=[[],[]]
for c in range(7):
    n=int(input(f'Digite o {c+1}° número: '))
    num[0].append(n) if n % 2 == 0 else num[1].append(n)
print('+'*22,f'\nNúmeros pares digitados:{sorted(num[0])}\nNúmero ímpares digitados:{sorted(num[1])}.')    
