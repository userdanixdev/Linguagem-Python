#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Versão 05:   Versão complexa com estrutura 'for'

lista=[]
while True:
    numero=int(input('Digite um valor para adicionar na lista: '))
    if numero not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(numero)
    else:
        print('Valor duplicado! Não será adicionado...')
    opcao=input('Deseja continuar?[S/N]').upper().strip()
    while opcao != 'S' and opcao != 'N':
        print('Opção incorreta. Informa novamente: ')
        opcao=input('Deseja continuar?[S/N]').upper().strip()
    if opcao == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')    
        
   

