#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Versão 03:

lista=[1,2,3,4,5,6,7,8,9,10]
while True:
  numero=int(input('Digite um valor inteiro: '))
  a=lista.count(numero)
  if a == 0:
    lista.append(numero)
    print('Número adicionado com sucesso.')
  else:
    print('Você já adicionou esse número...')
  resposta= input('Deseja continuar? [S/N] ')
  while resposta not in 'SsNn':
    resposta=input('Resposta inválida. Deseja continuar? [S/N] ')
  if resposta in 'Nn':
    break
print(f'Os números na ordem crescente foram: {sorted(lista)}.)

    
