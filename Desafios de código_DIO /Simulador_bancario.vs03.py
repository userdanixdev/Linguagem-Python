# Simulador Bancário
# Versão 03:

import sys


# Declarações de variáveis, carga de dados:
saldo = 0           # Saldo atual
limite = 500        # Limite de saque
extrato = ""        # Histórico de Transações
numero_saques = 0   # Número de saques realizados
limite_saques = 3   # Número máximo de saques permitidos

# Título do programa:
print(f'{"="*50}\n{"Simulador Bancário":^48}\n{"="*50}')
# Estrutura de repetição constante sempre que verdade:
while True:
        opcao = (input('''
    [D] - DEPOSITAR                       
    [S] - SACAR
    [E] - EXTRATO
    [Q] - SAIR
    Escolha uma das opções acima: '''   )).upper()
        # Condicionais:
        if opcao == 'D':
            valor =float(input('Informe o valor do depósito: ')) # Obter o valor do depósito
            # Verificação se o valor do depósito é valido:
            if valor > 0:
                saldo = saldo + valor # Se o valor for maior que zero, adicione o valor do depósito ao saldo
                extrato = extrato + f'Depósito:R$ {valor:.2f}\n' #Adiciona transação do depósito ao extrato
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print('Operação falhou. Valor informado inválido.')
        # Opção de saque:
        elif opcao == 'S':
            valor = float(input('Informe o valor do saque: '))                           
            # Verificações de condicionais para saque:
            excedeu_saldo = valor > saldo  # Variável para um valor mais que o saldo
            excedeu_limite = valor > (saldo + limite) # Variável para verificar se o valor excedeu o saldo e o limite
            excedeu_saques = numero_saques >= limite_saques # Verificar se o número de saques foi atingido
            # Condicionais para as variáveis:
            if excedeu_saldo:
                print('Operação inválida por saldo insuficiente.')
            elif excedeu_limite:
                print('Operação inválida por limite de saque e saldo.')                
                print(f'Seu saldo disponível é de R$ {saldo:.2f} e seu limite de saque é de R$ {limite:.2f}.')
            elif excedeu_saques:
                print('Operação falhou por número de saques excedido.')                
            elif valor > 0:    # Se o valor for maior que zero, o saldo é subtraido
                saldo = saldo - valor
                extrato = extrato + f'Saque:R${valor:.2f}\n'  # Adiciona transação de saque ao histórico
                numero_saques = numero_saques + 1 # Número de saques recebe mais 1, com limite de 3.
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')                
            else:
                print('Operação inválida. O valor informado é inválido.')                
        # Exibir histórico de transações e saldo:
        elif opcao == 'E':
            print(f'{'+'*42}\n{"Extrato":^40}\n{'+'*42}\n{"Não foram realizadas transações"}\n'if not extrato else extrato)
            print(f'Saldo:R$ {saldo:.2f}\n{'+'*40}')
        elif opcao == 'Q':
            print('Obrigado por utilizar nossos serviços.\n Volte sempre!')
            exit()
        else:
            print('Operação Inválida. Selecione novamente a operação correta.')                                                    
            break
        # Veriável de controle de saída:
        continuar = input('\nDeseja continuar outra operação? [S/N]: ')
        while continuar.lower() not in ['s','n']:
            print('Operação Inválida. Selecione novamente a operação correta.') 
            continuar = input('\nDeseja realizar outra operação?[S/N]: ')                                                   
        if continuar.lower() == 'n':            
            print('Obrigado por utilizar nossos serviços.\n Volte sempre!')
            exit()


        
