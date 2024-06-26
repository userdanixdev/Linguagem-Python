# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Lista: Pares e Ímpares

# Versão 03:

lista_composta = [[],[]]
for c in range(7):
    n=int(input(f'Digite o {c+1}º número: '))
    lista_composta[0].append(n) if n % 2 == 0 else lista_composta[1].append(n)
print('-'*22,f'\nNúmeros pares:{sorted(lista_composta[0])}\nNúmeros ímpares:{sorted(lista_composta[1])}')        
