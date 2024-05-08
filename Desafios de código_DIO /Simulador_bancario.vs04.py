# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:21:15 2024

@author: US
"""
# Objetivo Geral:
    # Separar as funções existentes de saque, depósito e extrato em funções.
        # Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

# Desafio:
    # Deverá ser criada novas funções como criar usuário (cliente do banco)
            # criar conta corrente ( vincular com o usuário )

# Função de saque:
    # A função de saque deve receber os argumentos apenas por nome.

# Função de depósito:
    # a função de depósito deve receber apenas argumentos por posição

# Função de extrato:
    # A função de extrato deve receber argumentos por posição e nome.

# Novas funções:
    # Precisamos criar duas novas funções: criar usuário e criar conta corrente.

# Criar usuário (cliente):
    # O programa deve armazenar os usuários em uma lista, um usuário é composto
#           por: nome, data de nascimento, cpf e endereço.
        # Endereço formato: logradouro,numero,bairro, cidade/sigla, estado.
        # Não poderá cadastrar 2 usuários com o mesmo CPF.

# Criar conta corrente:
    # O programa deve armazenar contas em uma lista, a conta é composta por:
    #    agência,número da conta e usuário.
    # O número da conta é sequencial, iniciando em 1.
    # O número da agência é fixo: '0001'.
    # O usuário tem mais de uma conta, mas a conta deve pertencer somente a um usuário.
import textwrap

# A função textwrap é usada para formatar parágrafos de texto que se ajustam
# dentro de uma largura especificada na saída.
# Com a função textowrap.fill podeos formatar os parágrafos de acordo com o tamanho de linhas.
# Exemplo: texto = textwrap.fill(texto,width=40)

# Criar uma função menu()
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
# A linha do return solicita uma entrada para o usuário e aguarda a entrada do usuário.
# Depois que o usuário digita uma opção e pressiona Enter, essa entrada é atribuída à
# variável nomeada e é impressa na linha seguinte.
# 2º função:
# A função recebe os três parâmetros lembrando que o '/' indica que os 2 primeiros valores são posicionais e não podem ser passados como palavra-chave.
def depositar(saldo,valor,extrato,/):                                      
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n' # \t = tabulação horizontal. É usado para criar espaços uniformes entre o identificador da opção
        print('\nDepósito realizado com sucesso.')
    else:
        print('\nOperação falhou. O valor informado é inválido.')
    return saldo,extrato        # A função retorna uma tupla contendo o saldo atualizado e o extrato atualizado da conta.
# 3ºFunção:
# O '*'-(asterisco) - Indica que todos os argumentos após ele devem ser passados como palavr-chave ao chamar a função. Ou seja, devem ser especificados
# pelo nome ao chamar a função e não como argumentos posicionais. Todos são esperados como argumento nomeado. Isso garante que você tenha que especificar
# explicitamente o nome dos parâmetros ao chamar a função, tornando mais clara cada argumento em que o representa.
def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print('A operação falhou. Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('Operação falha. O valor de saque exede o limite.')
    elif excedeu_saques:
        print('Operação falha. Número máximo de saques excedido.')
    elif valor > 0:
        saldo = saldo - valor
        extrato = extrato + f'Saque: R$ {valor:.2f}'
        numero_saques = numero_saques + 1
        print('Saque realizado com sucesso.')
    else:
        print('Operação falhou. O valor informado é inválido.')
    return saldo,extrato
# 4º função:
# Parâmetros antes da '/' são posicionais. O '*' antes de extrato devem ser fornecidos como argumentos nomeados 
def exibir_extrato(saldo,/,*,extrato):
    print(f'{"="*50}\n{"Extrato":^48}\n{"="*50}')
    print('Não foram realizadas movimentações.'if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('='*50)

# 5ºFunção:
def criar_usuario(usuarios):
    cpf = input('Informe o CPF(somente números): ')
    usuario = filtrar_usuario(cpf,usuarios)  # Chama a função filtrar_usuario para verificar se já existe um usuário com o CPF fornecido.
    if usuario:
        print('Já existe usuário com esse CPF.')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaa): ')
    endereco = input('Informe o endereço(logradouro,nro - bairro - cidade/sigla estado): ')
    usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco})
    print('== Usuário criado com sucesso! ==')

# 6º Função:
def filtrar_usuario(cpf,usuarios):
    # usuarios em 'for usuario in usuarios' é uma lista pois está entre [].O 'usuario' é um dicionário que representa um usuário na lista.
    # usuario['cpf'] é a chave do dicionario 'usuario'. Se a chave do usuário for igual ao 'cpf' que estamos procurando cria uma nova lista
    # chamada usuarios filtrados nomeada como variável. Em cada iteração do loop´, um usuário é adicionado a esta lista somente se sua chave
    # 'cpf' for igual ao 'cpf' fornecido.
    # A variável lista 'usuarios_filtrados' conterá todos os usuários cujos CPFs são iguais ao CPF fornecido. Se não houver nenhum usuário
    # com o CPF fornecido a lista será vazia. Logo a função irá retornar a variável 'usuarios_filtrados' mostrando o primeiro elemento da lista [0]
    # Sem a condição 'if' resultará em erro caso não encontre o usuário, se a lista estiver vazia(se não houver usuários com CPF fornecido,
    # o retorno será 'None'.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf] #<- List comprehension
    return usuarios_filtrados[0] if usuarios_filtrados else None

# 7º Função:
def criar_conta(agencia,numero_conta,usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios) # Chama a função para verificar se há um usuário com o CPF fornecido.
    if usuario:
        print('== Conta criada com sucesso!==')
        return {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario}
    print('Usuário não encontrado, fluxo de criação de conta encerrado.')

# 8º Função:
def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
            """
        #linha = f"""  # '\' indica que a string continua na próxima linha. Forma de quebrar a linha, sem adicionar espaços em branco.
    ##Agência:\t{conta['agencia']}  # \t = Caractere de tabulação que é usado para garantir uma formatação uniforme na exibição de dados
    #C/C:\t\t{conta['numero_conta']}  # dois \t\t alinha as informações
    #Titular:\t{conta['usuario']['nome']}
        print('='*40)
        print(textwrap.dedent(linha))
# 9º Função: PRINCIPAL :: Encontra-se todos as chamadas, variáveis
def main():
    limite_saques = 3  # Constante
    agencia = '0001' # Constante
    saldo = 0
    limite = 1000
    extrato = '' #Vazio
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            saldo,extrato = depositar(saldo,valor,extrato)
        elif opcao == 's':
            valor = float(input('Infore o valor do saque: '))
            saldo,extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,)
        elif opcao == 'e':
            exibir_extrato(saldo,extrato=extrato)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas)+1
            conta = criar_conta(agencia,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break
        else:
            print('Operação inválida. Por favor selecione novamente a operação desejada.')
main() 
