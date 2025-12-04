# Simulador Bancário Básico - Versão 1.6 - Modelo Funcional 
 # Autor: Daniel
 # Data: 2024-06-15 21:19h
 # Descrição: Este código simula um sistema bancário mais complexo.
 # Permite depósitos, saques e exibição de extratos comum nas versões anteriores.
 # Possui um método de cadastro usuário, com validação do CPF. 
 # Essa versão possui listagem de cadastro de usuários na opção no MENU.
 # Obs: Essa versão diminui a complexidade e extensibilidade da função 'criar_usuario()'. Para isso foi criada a função 'filtrar_usuario()'
 # A versão 1.5 possui o serviço de 'nova conta'.
 # A listagem do usuário está mais completa com dados da conta e agência.
 # Única mudança: menu como função e executável no final. Última versão funcional.

import re
from datetime import datetime

usuarios = []    
contas = []

# Funcionalidade nova para a versão 1.5, realização de saque funcional.
def realizar_saque(conta, limite,LIMITE_SAQUES ):

    contador_valores_invalidos = 0
    contador_saldo_insuficiente = 0
    contador_limite_excedido = 0
    contador_excede_saques = 0
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
    saldo = conta['saldo']
    extrato = conta['extrato']
    n_saques = conta['n_saques']
    saques = conta['saques']
    
    while True:
            try:
                texto = input("Informe o valor do saque ou digite 'sair' para voltar ao MENU:  ").strip()
                if texto.lower()=='sair':
                    print('Voltando ao menu...\n\n')                
                    break
                valor = float(texto)
                if valor <= 0:
                    idx = contador_valores_invalidos % len(mensagens_valores_invalidos)
                    print(mensagens_valores_invalidos[idx])
                    contador_valores_invalidos += 1
                    continue
                # Não prossegue ainda para as regras do sistema
                # Variáveis das regras do sistema abaixo: IMPORTANTE
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saque = n_saques >= LIMITE_SAQUES
                if excedeu_saldo:
                    idx = contador_saldo_insuficiente % len(mensagens_saldo_insuficiente)
                    print(mensagens_saldo_insuficiente[idx])
                    contador_saldo_insuficiente += 1
                    continue
                elif excedeu_limite:
                    idx = contador_limite_excedido % len(mensagens_limite_excedido)
                    print(mensagens_limite_execedido[idx])
                    contador_limite_excedido += 1
                    continue
                elif excedeu_saque:
                    idx = contador_excede_saques % len(mensagens_excede_saques)
                    print(mensagens_excede_saques[idx])
                    contador_excede_saques += 1
                    continue
                # Até aqui, todas as validações foram passadas. Saque agora é permitido.
                else:
                    conta['saldo'] -= valor
                    conta['extrato'] += f'\nSaque: R$ {valor:.2f}\n'                                
                    conta['n_saques'] += 1
                    conta['transacoes'] += 1
                    #conta['saques'] +=1
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                break
            except ValueError:
                print('Informe valores positivos e numéricos.')             
                # Resetar contadores:
                contador_valores_invalidos = 0
                contador_saldo_insuficiente = 0
                contador_limite_excedido = 0
                contador_excede_saques = 0
            except ValueError:
                print('Entrada inválida. Digite somente números inteiros.')  
                
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

    return conta, limite,LIMITE_SAQUES 
# Funcinalidade para a versão 1.5: Criação da conta
n_conta = len(contas) + 1
def criar_conta(agencia, n_conta, usuarios, contas):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    conta_existente = verificar_conta(cpf,contas)
    if conta_existente:
        print('\n Já existe uma conta associada a este CPF. Não é possível criar uma conta.')
        return None
    if usuario:
        nova_conta = {'agencia':agencia,'numero_conta':n_conta,'usuario':usuario,'saldo':0,
                      'extrato':'','n_saques':0,'transacoes':0,'saques':0}
        contas.append(nova_conta)
        n_conta = len(contas)+1
        print('\n Conta criada com sucesso...')
        return nova_conta
    else:
        print('\nUsuário não encontrado. \nFluxo de criação encerrado.\nCrie um novo usuário para criar uma conta')
        return None

def verificar_conta(cpf, contas):
    for conta in contas:
        if 'usuario' in conta and conta ['usuario']['cpf']==cpf:
            return conta
    return None        
def listar_dados(cpf,contas):
    conta = verificar_conta(cpf,contas)
    if conta and conta ['transacoes'] > 0 and conta['saques'] > 0:
        usuario = conta['usuario']
        print(f"\nNome:{usuario['nome']}\nCPF:{usuario['cpf']}\nData de Nascimento:{usuario['data_nascimento']}\n"
              f"Cidade: {usuario['endereco']['cidade']} - {usuario['endereco']['estado']}\nBairro: {usuario['endereco']['bairro']}\n"
              f"Rua: {usuario['endereco']['rua']}\nNúmero da casa: {usuario['endereco']['numero_casa']}\n"
              f"Agência: {conta['agencia']}\nNúmero da conta: {conta['numero_conta']}\n")
    else:        
        print('\n Para listar os dados do correntista, é necessário realizar ao menos uma transação e um saque.')
# Função adicionada de filtro de usuário cadastrado para a versão 1.4
def filtrar_usuario(cpf,usuarios):
# Essa função cria uma lista de usuários que contém todos os usuários cadastrados cujo CPF corresponde ao CPF fornecido pelo usuário.
# Usa-se a técnica de list comprehension para tal fim.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
# Retornará o primeiro usuário da lista caso haja. Do contrário, se o CPF já estiver cadastrado, retorna 'none'.

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i])*(10-i) for i in range(9))
    primeiro_digito_verificador = 11 -(soma%11)
    primeiro_digito_verificador = 0 if primeiro_digito_verificador >= 10 else primeiro_digito_verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito_verificador = 11 - (soma % 11)
    segundo_digito_verificador = 0 if segundo_digito_verificador >= 10 else segundo_digito_verificador
    return cpf[-2:] == f'{primeiro_digito_verificador}{segundo_digito_verificador}'
usuarios = []

def criar_usuario():
    while True:
        cpf= input('Informe o CPF: ')                         
        if validar_cpf(cpf):
            print('CPF válido.')
            break
        else:
            print('CPF inválido. Tente novamente.')
    if filtrar_usuario(cpf, usuarios): # Função nova para a versão 1.4 e seus argumentos obrigatórios.
        print('\n Já existe usuário com esse CPF. ')
        return None 
    while True:
        nome_usuario = input('Informe o nome Completo:  ')            
        if nome_usuario.replace(' ', '').isalpha():
            nome = ' '.join([nome.capitalize() for nome in nome_usuario.split()])
            break
        else:
            print('Nome inválido. Informe apenas letras.')
    while True:
        data_nascimento = input('Informe a data de nascimento:  ')
        padrao_data = r'^\d{1,2}/\d{1,2}/\d{4}$'                
        if re.match(padrao_data,data_nascimento):
            dia,mes,ano = map(int,data_nascimento.split('/'))
            try:
                data = datetime(ano, mes, dia)
                print(f'Data de nascimento válida: {data_nascimento}')
                break
            except ValueError:
                print('Data inválida. Informe uma data válida somente.')
        else:
            print('Formato inválido. Informe o formato correto: d/m/aaaa.')                    
    while True:
        cidade_estado = input('Informe a cidade e o estado: ')                
        padrao_cidade_estado = r'^[A-Za-z\s]+ - [A-Z]{2}$'
        if re.match(padrao_cidade_estado, cidade_estado):
            cidade, estado = cidade_estado.split(' - ')
            cidade = cidade.strip()
            estado = estado.strip()
            break
        else:
            print('Formato inválido. Informe no formato: cidade - Estado ( Ex: São Paulo - SP)')
    while True:
        bairro = input('Informe o bairro: ')
        if bairro.replace(' ', '').isalpha():
            break
        else:
            print('Bairro inválido. Informe apenas letras.')                
    while True:
        rua = input('Informe a rua:  ')                
        if rua.replace(' ', '').isalpha():
            break
        else:
            print('Rua inválida. Informe apenas letras.')
    while True:
        try:
            numero_casa = int(input('Informe o número da casa:  '))                
            break
        except ValueError:
            print('Número de casa inválido. Informe um número válido.')
        # Montagem do endereço:
    endereco = {'cidade': cidade, 'estado':estado, 'bairro':bairro, 'rua':rua,'numero_casa':numero_casa}
    usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco})                
    print('\nUsuário criado com sucesso.\n')
            
    return usuarios            
def exibir_extrato(saldo,/,*,extrato):

    print(f'{"+"*30}\n{"Extrato":^28}\n{"+"*30}')
    print('\nNão foram realizadas movimentações.\n'if not conta['extrato']else conta['extrato'])
    print(f'\nSaldo:\t\tR$ {conta['saldo']:.2f}')
    print("-"*30)  
    
    return saldo, extrato
# Função 'mostrar_menu()' 
def mostrar_menu():
    while True:
        print("""
    
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nu] Novo Usuário
[nc] Nova Conta
[q]  Sair
[ld] Lista Correntista
\n\n
""")
        opcao = input("Digite aqui: ").strip().lower()
        if opcao == 'd': # Melhoramento da função de depósito, a partir da versão 1.5
            cpf = input('Informe o CPF: ')
            conta = verificar_conta(cpf,contas)
            if not conta:
                print('\n❌ Nenhum usuário encontrado com esse CPF.')
                print('➡ Parece ser seu primeiro acesso.')
                print('👉 Cadastre o usuário e abra uma conta antes de realizar depósitos.\n')
                continue  # Volta ao menu principal
            while True:
                    try:
                        valor = float(input('Informe o valor do depósito: '))
                        if valor > 0:
                            conta['saldo'] += valor
                            conta['extrato'] += f'Depósito: R$ {valor:.2f}\n'
                            conta['transacoes']+= 1
                            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
                            break
                        else:
                            print('Operação falhou! O valor informado é inválido.')
                    except ValueError:
                        print('Operação falhou! Por favor, insira um valor numérico válido.')                    
        elif opcao == 's':  # Obs: A função de converter os caracteres para minúsculo e remoção de espaços estão no input do menu
            cpf = input('Informe o CPF: ')
            conta = verificar_conta(cpf,contas)
            if conta:
                realizar_saque(conta,limite,LIMITE_SAQUES)
            else:
                print('Nenhuma conta encontrada para o CPF informado. Por favor crie uma conta primeirao.')            
        elif opcao == 'e':            
    # Opção de extrato reformulada para versão 1.5
            cpf = input('Informe o CPF: ')
            conta = verificar_conta(cpf, contas)
            if conta:
                exibir_extrato(conta,extrato=extrato)
            else:
                print('Nenhuma conta encontrada para o CPF informado.\n Por favor crie uma conta e um novo usuário.')         
    # Opção de criar usuário. Sem alteração.        
        elif opcao == 'nu':
            criar_usuario()  
        elif opcao == 'ld':   # Para a versão 1.5, opção 'lu' mudou para 'ld'
            cpf = input('Informe o CPF:  ')
            listar_dados(cpf,contas)
            
        elif opcao == 'nc':  # Opção 'nova conta' criada para a versão 1.5
            agencia = '0001'            
            numero_conta = f'{len(contas)+1:06d}'
            criar_conta(agencia,n_conta, usuarios, contas)
        elif opcao == 'q':  # Opção de saída. Sem alteração.
            print('Encerrando o programa.')
            break
            import os
            exit()
        else:
            print('Operação inválida. Selecione a opção correta.')
        
mostrar_menu()        
                        

     

           
         
 
