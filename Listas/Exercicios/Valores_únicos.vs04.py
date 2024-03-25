#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista=[1,2,3,4,5,6,7,8,9,10]
while True:
    numero=int(input('Digite um número para adc na lista: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado, sem duplicatas.')
    else:
        print('Valor duplicado')
    resposta=input('Deseja continuar?[S/N]').upper().strip()
    while resposta != 'S' and resposta != 'N':
        resposta=input('Opção inválida. Informe novamente.\nQuer continuar?[S/N].').upper().strip()
    if resposta == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}.')



