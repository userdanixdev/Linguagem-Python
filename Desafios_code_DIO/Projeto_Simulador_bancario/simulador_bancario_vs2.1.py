# Com validação de entrada para nova conta, função de validação CPF.
# Versão 2.1:

import re
from datetime import datetime

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito_verificador = 11 - (soma % 11)
    primeiro_digito_verificador = 0 if primeiro_digito_verificador >= 10 else primeiro_digito_verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito_verificador = 11 - (soma % 11)
    segundo_digito_verificador = 0 if segundo_digito_verificador >= 10 else segundo_digito_verificador
    return cpf[-2:] == f'{primeiro_digito_verificador}{segundo_digito_verificador}'

usuarios = []

def criar_usuario():
    while True:
        cpf = input('Informe o CPF: ')
        if validar_cpf(cpf):
            print('CPF válido.')
            break
        else:
            print('CPF inválido. Tente novamente.')
    
    usuario_existe = False
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('\nJá existe usuário com esse CPF')
            usuario_existe = True
            break
    
    if not usuario_existe:
        while True:
            nome_usuario = input('Informe o nome completo: ')
            if nome_usuario.replace(' ', '').isalpha():
                nome = ' '.join([nome.capitalize() for nome in nome_usuario.split()])
                break
            else:
                print('Nome inválido. Informe apenas letras.')
        
        while True:
            data_nascimento = input('Informe a data de nascimento: ')
            padrao_data = r'^\d{1,2}/\d{1,2}/\d{4}$'
            if re.match(padrao_data, data_nascimento):
                dia, mes, ano = map(int, data_nascimento.split('/'))
                try:
                    data = datetime(ano, mes, dia)
                    print(f'Data de nascimento válida: {data_nascimento}')
                    break
                except ValueError:
                    print('Data Inválida. Informe uma data válida.')
            else:
                print('Formato inválido. Informe o formato correto: d/m/a.')
        
        while True:
            cidade_estado = input('Informe a cidade e o estado: ')
            padrao_cidade_estado = r'^[A-Za-z\s]+ - [A-Z]{2}$'
            if re.match(padrao_cidade_estado, cidade_estado):
                cidade, estado = cidade_estado.split(' - ')
                cidade = cidade.strip()
                estado = estado.strip()
                break
            else:
                print('Formato inválido. Informe no formato: cidade - Estado (ex: São Paulo - SP).')
        
        while True:
            bairro = input('Informe o bairro: ')
            if bairro.replace(' ', '').isalpha():
                break
            else:
                print('Bairro inválido. Informe apenas letras.')
        
        while True:
            rua = input('Informe a rua: ')
            if rua.replace(' ', '').isalpha():
                break
            else:
                print('Rua inválida. Informe apenas letras.')
        
        while True:
            try:
                numero_casa = int(input('Informe o número da casa: '))
                break
            except ValueError:
                print('Número da casa inválido. Informe um número válido.')
        
        endereco = {'cidade': cidade, 'estado': estado, 'bairro': bairro, 'rua': rua, 'numero_casa': numero_casa}
        usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
        print('Usuário criado com sucesso')

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[q] Sair
=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

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
            except ValueError:
                print('Operação falhou. O formato do valor inválido.')
        
    elif opcao == 's':
        while True:
            try:
                valor = float(input('Informe o valor do saque: '))
                if valor <= 0:
                    print('Somente números positivos.')
                    continue
                excedeu_saldo = valor >  saldo
                excedeu_limite =  valor > limite
                excedeu_saque = numero_saques >= LIMITE_SAQUES
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
                break
            except ValueError:
                print('Informe valores positivos e numéricos.')
        
    elif opcao == 'e':
        print(f'{"+"*50}\n{"Extrato":^48}\n{"+"*50}')
        print('Não foram realizadas movimentações...' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        
    elif opcao == 'q':
        print('Encerrando o programa.')
        break

    elif opcao == 'nu':
        criar_usuario()

    else:
        print('Operação inválida. Selecione a opção correta.')

print('\nLista de Usuários: ')
for usuario in usuarios:
    print(f"\nNome: {usuario['nome']}\nCPF: {usuario['cpf']}\nData de Nascimento: {usuario['data_nascimento']}\n"
          f"Cidade: {usuario['endereco']['cidade']} - {usuario['endereco']['estado']}\nBairro: {usuario['endereco']['bairro']}\n"
          f"Rua: {usuario['endereco']['rua']}\nNúmero da casa: {usuario['endereco']['numero_casa']}")
