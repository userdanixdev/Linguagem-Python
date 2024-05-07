# Programa de Simulação de um Caixa Eletrônico:
# 1° Opções do menu
menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
"""
# Saldo incial e limites:
saldo = 0           # Saldo atual
limite = 500        # Limite de saque
extrato = ""        # Histórico de transações
numero_saques = 0   # Número de saques realizados
limite_saques = 3   # Número máximo de saques permitidos

# Loop Principal:
while True:
    # Exibir menu e abrir opções para o usuário:
    opcao = input(menu)
    # Opção de depósito:
    if opcao == 'D'or opcao == 'd':
        valor = float(input('Informe o valor do depósito: ')) # Obter valor do depósito
    # Verificar se o valor do depósito é valido:
        if valor > 0:
            saldo = saldo + valor # Adicionar o valor do depósito ao saldo
            extrato = extrato + f'Depósito: R$ {valor:.2f}\n' # Adicionar transação de depósito ao extrato
        else:
            print('Operação falhou. Valor informado inválido.')
    # Operação de saque:
    elif opcao == 'S'or opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        # Verificações condicionais para saque:
        excedeu_saldo = valor > saldo # verificar se o saque excedo o saldo
        excedeu_limite = valor > (saldo + limite) # verificar se o saque excede o saldo combinado e o limite
        excedeu_saques = numero_saques >= limite_saques # Verificar se o número de saques foi atingido
        if excedeu_saldo:
            print('Operação inválida por saldo insuficiente.')
        elif excedeu_limite:
            print('Operação inválida pelo saque exceder o limite.')
        elif excedeu_saques:
            print('Operação falha. Número máximo de saques excedido.')
        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + f'Saque:R$ {valor:.2f}\n' # Adicionar transação de saque ao histórico
            numero_saques = numero_saques +1
        else:
            print('Operação inválida. O valor informado é inválido.')
    # Exibir histórico de transaçõs e saldo:
    elif opcao == 'E' or opcao == 'e':
        print('+'*42)
        print(f'{"EXTRATO":^40}')
        print('+'*42)
        print('Não foram realizadas movimentações.'if not extrato else extrato) # Exibir mensagem se nenhuma transação foi feita
        print(f'Saldo:R$ {saldo:.2f}') # Exibir saldo atual
        print('+'*42)
    # sair do programa:
    elif opcao == 'Q' or 'q':
        break
    # Opção inválida:
    else:
        print('Operação inválida. Selecione novamente a operação correta.')
              
