#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Obs: Não pode valor duplicado.

numeros=list()
while True:    # Looping infinito, com break nesse caso.
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
         print('Valor duplicado! Não vou adicionar...')
    resposta=(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('+'*30)
print(f'Você digitou os valores {numeros}.')
# Necessário agora a ordem CRESCENTE # Etapa 02 abaixo:
numeros.sort()
print(f'Os valores na ordem crescente são: {numeros}.')







