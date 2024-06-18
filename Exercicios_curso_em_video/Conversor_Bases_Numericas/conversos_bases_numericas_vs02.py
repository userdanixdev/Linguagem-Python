# Conversor de bases numéricas:

# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

# Versão 02: Versão em que solicita input do usuário 3 vezes e depois o programa pergunta se quer continuar ou não.

while True:
    for _ in range(3):
        while True:
            try:
                numero = int(input('Digite um número inteiro: '))
                break
            except ValueError:
                print('Somente números inteiros.')
        print('''
        Escolha uma das bases para conversão:

            [ 1 ] - Converter para Binário
            [ 2 ] - Converter para Octal
            [ 3 ] - Converter para Hexadecimal
                        ''')
        while True:
            try:
                opcao=int(input('Sua opção: '))
                if opcao == 1:
                    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)}.')
                elif opcao == 2:
                    print(f'{numero} convertido para OCTAL é igual a {oct(numero)}.')
                elif opcao == 3:
                    print(f'{numero} convertido para para HEXADECIMAL é igual a {hex(numero)}.')
                else:
                    print('Opção inválida. tente novamente.')
            except ValueError:
                print('Por favor,insira números inteiros.')
    while True:                
        continuar = input('Deseja continuar? [1-SIM / 2-NÃO].')
        if continuar in ['1','2']:
            break
        else:
            print('Selecione corretamente a opção.')
    if continuar == '2':
        break
print('fim')
                
        
