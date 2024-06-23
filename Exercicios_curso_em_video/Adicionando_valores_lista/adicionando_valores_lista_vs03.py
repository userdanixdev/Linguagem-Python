# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Adicionando valores em uma lista:
# Versão 03:

valores = []
while True:
        n = int(input('Digite um valor: '))
        if n not in valores:
            valores.append(n)
            valores.sort()   # Já deixa a lista em ordem
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado não será incluso na lista.')
        resp = input('Deseja continuar? [S/N]').upper().strip()
        while resp not in 'SN':
            print('O valor digitado é inválido.')
            resp = input('Deseja continuar? [S/N]').upper().strip()
        if resp == 'N':
            break
print(f'Você digitou os valores {valores}.')        
