 # Simulador Bancário Básico - Versão 1.2
 # Autor: Daniel
 # Data: 2024-06-15
 # Descrição: Este código simula um sistema bancário simples que permite depósitos, saques e exibição de extratos.
 # Essa versão inclui mensagens rotativas para melhorar a experiência do usuário. Além de todas as especificações anteriores.

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

# Listas de mensagens (personalize como quiser):
mensagens_valores_invalidos = [
    'Operação falhou! O valor informado é inválido. Somente valores positivos são aceitos.',
    'Valor inválido! Tente um número maior que zero.',
    'Esse número não é aceitável para saque. Por favor, insira um valor positivo.',
    'Cuidado! Digite um valor válido para continuar a operação.'
]

mensagens_saldo_insuficiente = [
    'Operação falhou! Você não tem saldo suficiente,',
    'Saldo insuficiente! Verifique seu saldo antes de tentar novamente.',
    'Você não possui fundos suficientes para essa operação.',
    'Saldo negativo detectado! Por favor, deposite fundos antes de tentar novamente.'
]

mensagens_limite_excedido = [
    'Operação falhou! O valor do saque excede o limite.',
    'Limite de saque ultrapassado! Tente um valor menor.',
    'Valor acima do limite diário permitido para saques.',
    'Saque negado - ultrapassou o limite estabelecido.'
]

mensagens_excede_saques = [
    'Operação falhou! Número máximo de saques diários excedido.',
    'Limite de saques diários atingido! Tente novamente amanhã.',
    'Você já realizou o número máximo de saques permitidos para hoje.',
    'Saque não autorizado - limite diário de saques alcançado.',
    'Tente amanhã, quem sabe você tenha mais sorte!'
]

# Contadores que registram tentativas de cada tipo de tentativas:

contador_valores_invalidos = 0
contador_saldo_insuficiente = 0
contador_limite_excedido = 0
contador_excede_saques = 0

# Na versão 1.1, o código foi ajustado para incluir a funcionalidade de depósito.
while True:
    opcao = input(menu).strip().lower() # Converter para minusculo e remover espaços

    if opcao == 'd': # Melhoramento da função de depósito
        while True:
            try:
                valor = float(input('Informe o valor do deposito: '))
                if valor > 0:
                    saldo += valor
                    extrato += f'Depósito: R$ {valor:.2f}\n'
                    print('Depósito realizado com sucesso!')
                    break
                else:
                    print('Operação falhou! O valor informado é inválido.')
            except ValueError:
                print('Operação falhou! Por favor, insira um valor numérico válido.')
        
    elif opcao == 's': # a função de converter os caracteres para minusculo e remover espaços já estão no input do menu
        while True:
            try:
                texto = input("Informe o valor do saque ou digite 'sair' para voltar ao menu:  ").strip()
                if texto.lower()=='sair':
                    print('Voltando ao menu...')
                    break
                valor=float(texto)
                if valor <= 0:
                    idx = contador_valores_invalidos % len(mensagens_valores_invalidos)
                    print(mensagens_valores_invalidos[idx])
                    contador_valores_invalidos += 1
                    continue
                    # Não prossegue para as regras do sistema.
                # Variáveis das regras do sistema: IMPORTANTE
                excedeu_saldo = valor >  saldo
                excedeu_limite =  valor > limite
                excedeu_saque = numero_saques >= LIMITE_SAQUES                    
                if excedeu_saldo:
                    idx = contador_saldo_insuficiente % len(mensagens_saldo_insuficiente)
                    print(mensagens_saldo_insuficiente[idx])    
                    contador_saldo_insuficiente += 1
                    continue
                if excedeu_limite:
                    idx = contador_limite_excedido % len(mensagens_limite_excedido)
                    print(mensagens_limite_excedido[idx])    
                    contador_limite_excedido += 1
                    continue
                if excedeu_saques:
                    idx = contador_excede_saques % len(mensagens_excede_saques)
                    print(mensagens_excede_saques[idx])    
                    contador_excede_saques += 1
                    continue                                        
                # Chegou até aqui, então todas as validações foram passadas. Saque permitido.    
                    saldo -= valor
                    extrato += f'Saque: R$ {valor:.2f}\n'
                    numero_saques += 1  
                    print('Saque realizado com sucesso!')
                    # Resetar contadores (opcional)
                    contador_valores_invalidos = 0
                    contador_saldo_insuficiente = 0
                    contador_limite_excedido = 0
                    contador_excede_saques = 0
            except ValueError:
                print('Entrada inválida. Digite números inteiros')                    
                          
# Criação da função de extrato mais robusta        
    elif opcao == 'e':
        print('\n================ EXTRATO ================')
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
                     
            print(f'Saldo: R$ {saldo:.2f}')
        print('=========================================')
    elif opcao == 'q':
        break
        import os
        exit()
    else:
        print('Operacao invalida. Selecione a opção correta.')
        
