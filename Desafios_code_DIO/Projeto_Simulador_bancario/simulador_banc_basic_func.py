# Simulador Bancário versão funcional
# Feita pelo tutor Guilherme Carvalho - Analista de Sistemas - CEO - OAK Solutions


import textwrap

def  menu():

    menu = '''\n
        +++++++ MENU +++++++
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Contas
        [nu]\tNovo usuário
        [q]\tSair
        ++ => '''
    return input(textwrap.dedent(menu))

print(menu())

# '/' indica que todos os parâmetros são posicionais, eles não podem ser passados como argumentos nomeados
# quando a função é chamada.
def depositar(saldo,valor,extrato,/):  

    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print('\n Operação falhou. O valor informado é inválido.')

    return saldo, extrato        

# '*' o asterisco é um operador especial que indica que todos os parâmetros seguintes deve ser passados
# como argumentos nomeados(keyword arguments).Ou seja, você não pode passar esses parâmetros por posição
# Você deve especificar o nome do argumento ao chamá-los.
def sacar (*,saldo,valor,extrato,limite,numero_saques,limite_saques):

    excedeu_saldo =  valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print('\nOperação falhou. Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('\nOperação falhou. O valor do saque excede o limite.')
    elif excedeu_saques:
        print('\nOperação falhou. Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n==== Saque realizado com sucesso! ====')
    else:
        print('\nOperação falhou. O valor informado é inválido.')

    return saldo, extrato

# A '/' indica que todos os parâmetros antes dela -'Saldo'- são argumentos posicionais obrigatórios.
# Significa que ao chamar a função, você deve passar o argumento 'saldo' por posição e não pode passa-lo
# como argumento nomeado

# O '*' asterisco indica que todos os parâmetros após ele são argumentos nomeados obrigatórios.
# Isso significa que você deve passar 'extrato' como argumento nomeado e não pode passá-lo por posição.
#
# Exemplo: exibir_extrato(1000, extrato="Algum extrato") é válido,
# mas exibir_extrato(1000, "Algum extrato") não é válido.

# Chamada correta:
# exibir_extrato(1000, extrato="Depósito: R$ 500.00\nSaque: R$ 200.00\n")

# Chamada incorreta - saldo como argumento nomeado
# exibir_extrato(saldo=1000, extrato="Depósito: R$ 500.00\nSaque: R$ 200.00\n")  # Isso gerará um erro

def exibir_extrato(saldo,/,*,extrato):

    print(f'{"="*30}\n{"Extrato":^28}\n{"="*30}')
    print('Não foram realizadas movimentações.'if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print("="*30)

def criar_usuario(usuarios):

    cpf = input('Informe o CPF (somente número): ')
    # A variável 'usuario' chama a função 'filtrar_usuario' para verificar o cpf.
    # Se estiver, a função retorna o usuário, do contrário 'none'
    usuario =  filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\nJá existe usuário com esse CPF.')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd--mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro-bairro-cidade/silga estado): ')
    # Adiciona um dicionário com os dados do novo usuário a lista de usuários:
    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco})

    print('+++ Usuário com sucesso +++')

def filtrar_usuario(cpf,usuarios):

    #Cria uma lista usuarios_filtrados que contém todos os usuários na lista de usuarios cujo CPF
    # corresponde ao CPF fornecido. Usa uma list comprehension para filtrar os usuários.

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    # Retorna o primeiro usuário na lista usuarios_filtrados se houver algum usuário na lista
    # (ou seja, se o CPF já estiver cadastrado), caso contrário, retorna None.

def criar_conta(agencia,numero_conta, usuarios):

    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso. ===')
        return {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario}

    print('\n Usuário não encontrado, fluxo de criação de conta encerrado.')

def listar_contas(contas):

    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            '''
        print('+'*100)
        print(text.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            saldo,extrato =  depositar(saldo,valor,extrato)
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo,extrato = sacar(
                saldo = saldo,
                valor=valor,
                extrato=extrato,
                limite = limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,)

        elif opcao == 'e':
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação inválida. Por favor, selecione novamente a operação.')

main()            

    
           
