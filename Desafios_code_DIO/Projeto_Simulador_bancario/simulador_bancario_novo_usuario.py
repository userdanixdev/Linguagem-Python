# Novas opções: Nova opção de usuários

usuarios = []  # Variável vazia recebe lista vazia

while True:  # Loopíng infinito
    print('1.Criar usuário.')
    print('2.Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cpf = input('informe o CPF: ')
        usuario_existe = False
        for usuario in usuarios:
            if usuario['cpf'] == cpf:
                print('\nJá existe usuário com esse CPF')
                usuario_existe = True
                break
        if not usuario_existe:
            nome = input('Informe o nome completo: ')
            data_nascimento = input('Informe a data de nascimento: ')
            endereco = input('Informe o endereço: ')
            usuarios.append({'nome':nome,'data_nascimento':data_nascimento,'cpf':cpf,'endereco':endereco})
            print('Usuario criado com sucesso')
    elif opcao == '2':
        print('encerrando o programa')
        break
    else:
        print('Opcao inválida. Tente novamente.')
print('\nLista de Usuários: ')
for usuario in usuarios:
    print(f'Nome: {usuario['nome']},CPF:{usuario['cpf']},Data de Nascimento:{usuario['data_nascimento']},Endereço:{usuario['endereco']}')
        
        
