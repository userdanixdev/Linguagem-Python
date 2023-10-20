#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Versão 04:

lista=[]
resp=""
while resp in 'S':
    numero=int(input('Digite um número inteiro: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Esse número já existe!')
    resp=input('Deseja continuar? [S/N]').upper()
    if resp == 'N':
        break
print(sorted(lista))




