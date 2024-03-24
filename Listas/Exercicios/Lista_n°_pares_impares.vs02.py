#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Versão 02:

valores=[[],[]]
for contador in range(1,8):
    numero=int(input(f'Digite o valor {contador}°: '))
    valores[numero % 2].append(numero)
print(f'Valores pares digitados: {sorted(valores[0])}.')
print(f'Valores impares digitados: {sorted(valores[1])}.')
