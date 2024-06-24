# Normalmente, a agência é fixa ou escolhida previamente, então podemos definir um valor padrão para a agência. 
# O número da conta pode ser gerado incrementando uma variável global que mantém o controle do último número de conta gerado.

def criar_conta(agencia,usuarios):
  global ultimo_numero_conta
  cpf = input('Informe o CPF do usuário: ')
  usuario = filtrar_usuario(cpf,usuarios)
  if usuario:
      ultimo_numero_conta += 1
      numero_conta = ultimo_numero_conta
      print('Conta criada com sucesso.')
      conta = {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario}
      contas.append(conta)
      return conta

   print('\nUsuário não encontrado, fluxo de criação de conta encerrado.')
   return None
