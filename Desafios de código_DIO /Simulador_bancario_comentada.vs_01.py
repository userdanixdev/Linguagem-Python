# Operações de depósito:
# Apenas valores positivos
# Trabalhar apenas com 1 usuário - Inicialmente não iremos identificar número de agência e conta.
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação do extrato.

# Operação de saque:
  # O sistema deve permitir realizar 3 saques diários.
  # Limite de saque de R$ 300,00 por saque.
  # Caso não tenha saldo em conta, o sistema deve exibir uma mensagem informando a invalidez do saque.
  # Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de extrato:
  # Deve listar todos os depósitos e saques realizados na conta. 
  # Além disso, exibir o saldo atual da conta.
  # O formato é com duas casas decimais depois da vírgula ( R$ 000,00 )

menu = """
        [D] Depositar
        [S] Sacar
        [E] Extrato
        [Q] Sair
        """
saldo = 0     # Variável numérica iniciando com 0
limite = 500  # Variável numérica iniciando com 500
extrato = ''  # Variável vazia
numero_saques = 0 # Variável numérica iniciando com 0
limite_saques = 3 # Variável numérica limitada a 3 saques

while True:              # Looping sempre que verdade
    opcao = input(menu)  # Variável opcao recebe a variável menu, nela contem as opções que iremos colocar abaixo
    if opcao == 'D' or opcao == 'd':  # operador condicional que habilita a opção depositar em maiusclo ou minúsculo
        valor = float(input('Informe o valor do depósito: ')) # Usuário deve inserir o valor do depósito
        if valor > 0:       # Operador condicional aninhado se o valor inserido pelo usuário for maior que 0. 
            saldo += valor  # A variável com valor 0 recebe o valor colocado pelo usuário
            extrato += f'Depósito: R$ {valor:.2f}\n' # O extrato recebe o valorm também
        else:  # Com o else obrigado o valor a ser maior que zero se não a operação dará erro, inserir o else.
            print('Operação falhou. O valor informado é inválido.')
    elif opcao == 's' or opcao == 'S': # Continuação do looping do menu para 's' de sacar
        valor=float(input('Informe o valor do saque: ')) # Usuário deve inserir o valor de saque
        excedeu_saldo=valor > saldo     # Variável interna na condição elif para valor de saque maior que o saldo
        excedeu_limite = valor > limite # Variável interna declarada para valor é maior que o limite de saque
        excedeu_saques = numero_saques >= limite_saques # Variável que declara o excedente o limite de saque
        if excedeu_saldo: # Condicional para a variável com uma mensagem
            print('Operado falhou. Você não tem saldo suficiente.') # Valor de saque maior do que o saldo
        elif excedeu_limite: # Condicional para a variável que o saque excede o limite
            print('Operação falhou. O valor do saque excede o limite.')
        elif excedeu_saques: # Condicional para a variável em que o numero de saques é igual ou maior que o limite de saque
            print('Operação falhou. Número máximo de saques excedido.')
        elif valor > 0: # Condicional para valor maior que zero no modo sacar
            saldo -= valor # Ao sacar o saldo é subtraido recebendo o saldo menos o valor
            extrato += f'Saque: R$ {valor:.2f}\n' # Extrato recebe o valor
            numero_saques += 1 # Número de saques limitado a 3, recebe 1
        else:
            print('Operação falhou! Valor informado inválido.') # Qualquer operação inválida, exibe essa mensagem
    elif opcao == 'e' or opcao == 'E': # Opção de visualizar extrato, sem inputs do usuário
        print(f'{'='*30}\n{"Extrato":^28}\n{'='*30}')
        print('Não foram realizadas movimentações.\n'+f'Saldo: R${saldo:.2f}')
    elif opcao == 'q' or opcao == 'Q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
