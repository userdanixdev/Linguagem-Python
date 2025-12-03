# Simulador Bancário Básico
# Versão 1.1
# 1. Menu Simples
# 2. Insere estrutura de repetição e condicionais com tratamento de erros.
# 3. Novas validações de entrada, robustes nas opções e novas variáveis com regras para o sistema.

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
# Na versão 1.1, o código foi ajustado para incluir a funcionalidade de depósito.
while True:
    opcao = input(menu).strip().lower() # Converter para minúsculo e remover espaços extras
    # Melhoramento da função de depósito
    if opcao == 'd':
        while True:
            try:
                valor = float(input('Informe o valor do depósito: '))
                if valor > 0:
                    saldo += valor
                    extrato += f'Depósito: R$ {valor:.2f}\n'
                    print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
                    break
                else:
                    print('Operação falhou. O valor informado inválido.')
            except ValuerError:
                print('Operação falhou. O formato do valor inválido.')
        
    elif opcao == 's': # A função de converter os caracteres para minusculo e remover espaços já estão no input do menu.
        while True:
            try:
                valor = float(input('Informe o valor do saque: '))
                if valor <= 0:
                    print('Somente números positivos.')
                    continue
                # Variáveis:
                excedeu_saldo = valor >  saldo
                excedeu_limite =  valor > limite
                excedeu_saque = numero_saques >= LIMITE_SAQUES
                # Condicionais:
                if excedeu_saldo:
                    print('Operação falhou. Você não tem saldo suficiente')
                elif excedeu_limite:
                    print('Operação falhou. O valor do saque excede o limite.')
                elif excedeu_saque:
                    print('Operação falhou. Número máximo de saques excedido.')
                else:
                    saldo -= valor
                    extrato += f'Saque: R$ {valor:.2f}\n'
                    numero_saques += 1
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                break  # Sai do loop após operação bem-sucedida ou falha;
            except ValueError:
                print('Informe valores positivos e numéricos.')
        
        print('Sacar')
    elif opcao == 'e':
# Criação da função de extrato mais robusta
        print(f'{"+"*50}\n{"Extrato":^48}\n{"+"*50}')
        print('Não foram realizadas movimentações...'if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('Extrato')
    elif opcao == 'q':
        break
        import os
        exit()
    else:
        print('Operacao inválida. Selecione a opção correta.')
        
    
