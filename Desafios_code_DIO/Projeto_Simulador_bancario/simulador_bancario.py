# Simulador Bancário:

menu = '''
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        => '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Deposito')
    elif opcao == 's':
        print('Sacar')
    elif opcao == 'e':
        print('Extrato')
    elif opcao == 'q':
        break
    else:
        print('Operacao invalida. selecione a opcao correta.')
        
    
