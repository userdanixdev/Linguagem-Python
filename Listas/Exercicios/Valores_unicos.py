#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Obs: Não pode valor duplicado.

lista=list()
while True:
  numbers=int(input('Digite um valor: '))
  if numbers not in lista:
    lista.append(numbers)
    print('Valor adicionado com sucesso.')
  else:
    print('Valor duplicado. Não será adicionado.')
  pergunta=input('Quer continuar? [S/N] ')
  if pergunta not in 'SsNn':
    pergunta=input('Resposta inválida. Quer continuar? [S/N] ')
  if pergunta in 'Nn':
    break
print('='*30)
print(f'Você digitou os valores {lista}.')
lista.sort()
print(f'Os valores na ordem crescente são: {lista}.')



