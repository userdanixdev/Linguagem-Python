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

# Versão 03:  
import sys
from time import sleep
print(f'{'='*50}\n{"Simulador Bancário Versão 3.1":^48}\n{'='*50}')
# Declarar variáveis iniciais e limites:
saldo = 0         #Saldo atual do usuário
limite = 500      # Usuário tem um limite máximo de saque
extrato = ''      # Exibir extrato, variável vazia
numero_saques = 0 # Variável numérica inicial contadora
limite_saques = 3 # Número máximo de saques permitidos
# Looping de repetição sempre que verdade:
while True:
    opcao=' '
    while opcao not in 'dseq':
        opcao = input('''

    [D]- Depositar
    [S]- Sacar
    [E]- Extrato
    [Q]- Sair ''').upper()  # Caso o usuário digite as opções em letra minúscula, irá retornar maiúscula.

    # Opção de depósito:
        if opcao == 'D':
            valor = float(input('Informe o valor do depósito: ')) # Usuário deve inserir o valor de depósito
    # Verificação se o valor do depósito é válido:
            if valor > 0:
                saldo = saldo + valor # Adicionar o valor do depósito ao saldo
                extrato = extrato + f'Depósito: R$ {valor:.2f}\n' # Adicionar a transação de depósito ao extrato
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso.') # Mostrar ao usuário o resultado
            else:
                print(f'Operação falhou. Valor informado inválido.') # Mostrar ao usuário valores inválidos
    # Opção de saque:
        elif opcao == 'S':
            valor = float(input('Informe o valor de saque: ')) # variável valor para usuário informar o valor
            # Verificações condicionais para saque:
            excedeu_saldo = valor > saldo # declara que o valor de saque é maior que o saldo
            excedeu_limite = valor > (saldo+limite) # declara que o valor de saque é maior que o limite de saque
            excedeu_saques = numero_saques >= limite_saques # Declara que o número de saques é excedido se for maior ou igual a 3
            if excedeu_saldo:
                print('Operação inválida por saldo insuficiente.')
            elif excedeu_limite:
                print('Operação inválida. Saque acima do limite permitido.')
            elif excedeu_saques:
                print('Operação inválida. Número máximo de saques excedido no dia.')
            elif valor > 0:
                saldo = saldo - valor # saldo é subtraido do valor para saque em opção s
                extrato = extrato + f'Saque: R$ {valor:.2f}\n'
                numero_saques = numero_saques + 1 # Número de saques limitado a 3 recebe 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            else:
                print('Operação inválida. O valor informado é inválido.')
# Exibir histórico de transações e saldo, opção no menu E:
        elif opcao == 'E':
            print(f'{'+'*40}\n{"Extrato":^38}\n{'+'*40}')
            print('Não foram realizadas movimentações.'if not extrato else extrato) # Exibir mensagem se nenhuma transação foi feita
            print(f'Saldo:R$ {saldo:.2f}')  # Exibir saldo atual na opção e de extrato.
            print('+'*40)
# Sair do programa:
        elif opcao == 'Q':
            print('Saindo do programa.. Até logo.')
            sleep(2)
            exit()
     
