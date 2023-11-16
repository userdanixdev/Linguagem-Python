#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Versão 03:

lista=[]
while True:
    numero=int(input('Digite um número inteiro: '))
    a=lista.count(numero)
    if a == 0:
        lista.append(numero)
        print('Número adicionado com sucesso!')
    else:
        print('Você já adicionou esse número...')
    resposta=input('Deseja continuar? [S/N]')
    while resposta not in 'SsNn':
        resposta = input('Quer continuar?[S/N]')  # Irá fazer looping infinito até digitar ou 's','S','N','n'
    if resposta in 'nN':
        break
nova_lista=sorted(lista)
print(f'Os números que você digitou foram: {nova_lista} em ordem crescente.')

Resultado no console:

Digite um número inteiro: 456
Numero adicionado com sucesso.
Deseja continuar?[S/N]r
Quer continuar?[S/N]r
Quer continuar?[S/N]s
Digite um número inteiro: 123
Numero adicionado com sucesso.
Deseja continuar?[S/N]s
Digite um número inteiro: 689
Numero adicionado com sucesso.
Deseja continuar?[S/N]p
Quer continuar?[S/N]n
Os números que vc digitou foram [123, 456, 689].
=============================================================================





