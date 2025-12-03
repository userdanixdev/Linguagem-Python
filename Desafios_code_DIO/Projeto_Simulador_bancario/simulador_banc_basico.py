# Simulador Bancário Básico:
# 1. Menu simples
# 2. Variáveis contadoras e limitadas
# 3. Estruturas de repetição e condicionais simples, sem tratamento de erros.

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
        
    
