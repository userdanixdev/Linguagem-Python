# Projeto Simulador Bancário:

import re
from datetime import datetime
usuarios = []
contas = [] 

def filtrar_usuario(cpf,usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

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
          
def validar_cpf(cpf):

    cpf = re.sub(r'\D','',cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i)for i in range(9))
    primeiro_digito_verificador = 11 - (soma % 11)
    primeiro_digito_verificador = 0 if primeiro_digito_verificador >= 10 else primeiro_digito_verificador
    soma = sum(int(cpf[i])* (11 - i) for i in range(10))
    segundo_digito_verificador = 11 - (soma % 11)
    segundo_digito_verificador = 0 if segundo_digito_verificador >= 10 else segundo_digito_verificador
    return cpf[-2:] == f'{primeiro_digito_verificador}{segundo_digito_verificador}'

def exibir_extrato(saldo,/,*,extrato):

    print(f'{"+"*30}\n{"Extrato":^28}\n{"+"*30}')
    print('\nNão foram realizadas movimentações.\n'if not conta['extrato']else conta['extrato'])
    print(f'\nSaldo:\t\tR$ {conta['saldo']:.2f}')
    print("-"*30)

def verificar_conta(cpf,contas):

    for conta in contas:
        if 'usuario' in conta and conta['usuario']['cpf']==cpf:
            return conta
    return None

def realizar_saque(conta,limite,LIMITE_SAQUES):

    saldo = conta['saldo']
    extrato = conta['extrato']
    numeros_saques = conta['numeros_saques']
    saques = conta['saques'] 

    while True:
        try:
            valor = float(input('Informe o valor do saque: '))
            if valor <= 0:
                print('Somente números positivos.')
                continue
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                print('Operação falhou. Você não tem saldo suficiente.')       
            elif excedeu_limite:
                print('Operação falhou. O valor de saque excede o limite.')                
            elif excedeu_saque:
                print('Operação falhou. Número máximo de saques excedido.')
            else:
                conta['saldo'] -= valor
                conta['extrato'] += f'\nSaque: R$ {valor:.2f}\n'                                
                conta['numeros_saques'] += 1
                conta['transacoes'] += 1
                conta['saques']+=1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            break
        except ValueError:
            print('Informe valores positivos e numéricos.')                

def criar_conta(agencia,numero_conta,usuarios,contas):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios)
    # Atualização : Verifica se já existe uma conta associada ao CPF
    conta_existente = verificar_conta(cpf,contas)
    if conta_existente:
        print('\n Já existe uma conta associada a este CPF. Não é possível criar uma conta.')
        return None
    if usuario:
        nova_conta = {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario,'saldo':0,
                      'extrato':'','numeros_saques':0,'transacoes':0,'saques':0}
        contas.append(nova_conta)
        print('\nConta criada com sucesso...')
        return nova_conta
    else:
        print('\nUsuário não encontrado. Fluxo de criação encerrado.\nCrie um novo usuário para criar uma conta')
        return None
            
def criar_usuario():
    while True:
        cpf=input('Informe o CPF: ')
        if validar_cpf(cpf):
            print('\nCPF válido.')
            break
        else:
            print('\nCPF inválido. Tente Novamente.')
    if filtrar_usuario(cpf,usuarios):
        print('\nJá existe usuário com esse CPF.')            
        return
    while True:
        nome_usuario = input('Informe o nome completo: ')
        if nome_usuario.replace(' ','').isalpha():
            nome =' '.join([nome.capitalize() for nome in nome_usuario.split()])
            break
        else:
            print('Nome inválido. Informe apenas letras.')
    while True:
        data_nascimento = input('Informe a data de nascimento: ')            
        padrao_data = r'^\d{1,2}/\d{1,2}/\d{4}$'
        if re.match(padrao_data, data_nascimento):
            dia,mes,ano = map(int,data_nascimento.split('/'))
            try:
                data =  datetime(ano,mes,dia)
                print(f'Data de nascimento válida: {data_nascimento}')
                break
            except ValueError:
                print('Data inválida. Informe uma data válida.')
        else:
            print('Formato inválido. Informe o formato correto: d/m/a')                
    while True:
        cidade_estado = input('Informe a cidade e o estado: ')
        padrao_cidade_estado = r'^[A-Za-z\s]+ - [A-Z]{2}$'
        if re.match(padrao_cidade_estado,cidade_estado):
            cidade,estado =  cidade_estado.split('-')
            cidade = cidade.strip()
            estado = estado.strip()
            break
        else:
            print('\nFormato inválido. Informe no formato: cidade - Estado(São Paulo - SP)')
    while True:
        bairro = input('Informe o bairro: ')
        if bairro.replace(' ','').isalpha():
            break
        else:
            print('\nBairro inválido. Informe apenas letras.')
    while True:
        rua = input('Informe a rua: ')
        if rua.replace(' ','').isalpha():
            break
        else:
            print('Rua inválida. Informe apenas letras.')
    while True:
        try:
            numero_casa=int(input('Informe o número da casa: '))                                            
            break
        except ValueError:
            print('Número da cada inválido. Informe um número válido.')
    endereco = {'cidade': cidade,'estado':estado,'bairro':bairro,'rua':rua,'numero_casa':numero_casa}
    usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco})
    print('Usuário criado com sucesso.')                        





menu = '''

        [d] - Depositar
        [s] - Sacar
        [e] - Extrato
        [nu]- Novo usuário
        [nc]- Nova conta
        [ld]- Listar dados do Correntista
        [q] - Sair
        => '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()
    if opcao == 'd':
        cpf = input('Informe o CPF: ')
        conta = verificar_conta(cpf,contas)
        if conta:
            while True:
                try:
                    valor=float(input('Informe o valor do depósito: '))
                    if valor > 0:
                        conta['saldo'] += valor
                        conta['extrato'] += f'Depósito: R$ {valor:.2f}\n'
                        conta['transacoes']+= 1
                        print(f'Depósito de R$ {valor:.2f} realizado com sucesso')
                        break
                    else:
                        print('Operação falhou. O valor informado inválido.')
                except ValueError:
                    print('Operação falhou. O valor informado inválido.')
        else:
            print('Conta não encontrada. Crie uma conta primeiro para realizar depósitos.')
    elif opcao == 's':
        cpf = input('Informe o CPF: ')
        conta =  verificar_conta(cpf,contas)
        if conta:
            realizar_saque(conta,limite,LIMITE_SAQUES)
        else:
            print('Nenhuma conta encontrada para o CPF informado. Por favor crie uma conta primeiro.')                                            

    elif opcao == 'e':
        cpf = input('Informe o CPF: ')
        conta =  verificar_conta(cpf,contas)
        if conta:
            exibir_extrato(conta,extrato=extrato)
        else:
            print('Nenhuma conta encontrada para o CPF informado.\n Por favor crie uma conta e um novo usuiário.')                        
    elif opcao == 'q':
        print('Encerrando o programa')
        break
    elif opcao == 'nu':
        criar_usuario()
    elif opcao == 'nc':
        agencia = '0001'
        numero_conta = f'{len(contas)+1:06d}'
        criar_conta(agencia,numero_conta,usuarios,contas)
    elif opcao == 'ld':
        cpf=input('Informe o CPF: ')                            
        listar_dados(cpf,contas)
    else:
        print('Operação inválida. Selecione a opção correta.')

