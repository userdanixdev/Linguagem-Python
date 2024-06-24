# Novas opções: Nova opção de usuários

import re
from datetime import datetime
usuarios = []  # Variável vazia recebe lista vazia

# Em python, as funções devem ser definidas antes de serem chamadas.
def validar_cpf(cpf):

    # remove caracteres não numéricos:
    cpf = re.sub(r'\D', '',cpf)
    # Verifica se o CPF tem 11 dígitos:
    if len(cpf) != 11:
        return False
    # Verifica se todos os dígitos são iguais (caso especial de CPF inválido)
    if cpf == cpf[0]*11:
        return False
    # Cálculo do primeiro dígito verificador:
    soma = sum(int(cpf[i])*(10-i)for i in range(9))
    primeiro_digito_verificador = 11 - (soma%11)
    primeiro_digito_verificador = 0 if primeiro_digito_verificador >= 10 else primeiro_digito_verificador
    # Cálculo do segundo digito verificador:
    soma = sum(int(cpf[i])*(11-i)for i in range(10))
    segundo_digito_verificador = 11 - (soma%11)
    segundo_digito_verificador = 0 if segundo_digito_verificador >= 10 else segundo_digito_verificador
    # Verifica se os dígitos verificadores estão corretos:
    return cpf[-2:] ==  f'{primeiro_digito_verificador}{segundo_digito_verificador}'

while True:  # Loopíng infinito
    print('1.Criar usuário.')
    print('2.Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
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
                    if nome_usuario.replace(' ','').isalpha():  # 'isalpha verifica se contem apenas letras
                        nome =' '.join([nome.capitalize() for nome in nome_usuario.split()])
                        break
                    else:
                        print('Nome inválido. Informe apenas letras.')
            while True:                        
                    data_nascimento = input('Informe a data de nascimento: ')
                    padrao_data = r'^\d{1,2}/\d{1,2}/\d{4}$'
                    if re.match(padrao_data, data_nascimento):  # Verifica se a entrada do usuario corresponde ao padrão da expressão regular
                        # Se a data corresponder ao padrão, prosseguimos:
                        dia,mes,ano=map(int,data_nascimento.split('/')) # Divide a string 'data_nascimento' usando split '/' e converte para inteiros;
                        # Verificar se a data é valida:
                        try:
                            data = datetime(ano,mes,dia)  # A variável data recebe formato datetime com o ano,mes,dia.
                            print(f'Data de nascimento válida: {data_nascimento}')
                            break
                        except ValueError:
                            print('Data Inválida. Informe a data válida.')
                    else:
                        print('Formato inválido. Informe o formato correto: d/m/a.')
            while True:                        
                cidade_estado = input('Informe a cidade e o estado: ')
                padrao_cidade_estado = r'^[A-Za-z\s]+ - [A-Z]{2}$'
                if re.match(padrao_cidade_estado,cidade_estado):
                    cidade,estado = cidade_estado.split('-')
                    break
                else:
                    print('Formato inválido. Informe no formato: cidade - Estado (ex: São Paulo - SP).')
            while True:
                bairro = input('Informe o bairro: ')
                if bairro.replace(' ','').isalpha():
                    break
                else:
                    print('Bairro inválido. Informe apenas letras.')
            while True:
                rua = input('Informe a rua: ')
                if rua.replace(' ','').isalpha():
                    break
                else:
                    print('Rua inválida. Informe apenas letras.')
            while True:
                try:
                    numero_casa = int(input('Informe o número da casa: '))
                    break
                except ValueError:
                    print('Número da casa inválido. Informe um número valido.')
            endereco = {'cidade':cidade,'estado':estado,'bairro':bairro,'rua':rua,'numero_casa':numero_casa}                    
            usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco})
            print('Usuario criado com sucesso')
    elif opcao == '2':
        print('encerrando o programa')
        break
    else:
        print('Opcao inválida. Tente novamente.')
print('\nLista de Usuários: ')
for usuario in usuarios:
    print(f'\nNome: {usuario['nome']},\nCPF:{usuario['cpf']},\nData de Nascimento:{usuario['data_nascimento']},\nEndereço:{usuario['endereco']}\n'
          f'\nCidade: {usuario['endereco']['cidade']} - {usuario['endereco']['estado']}\nBairro: {usuario['endereco']['bairro']}\n'
          f'\nRua: {usuario['endereco']['rua']}\nNúmero da casa: {usuario['endereco']['numero_casa']}')
        

