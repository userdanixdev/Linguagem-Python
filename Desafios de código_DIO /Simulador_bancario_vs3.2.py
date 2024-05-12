# Versão 3.2 Com funções
import textwrap

def menu():
 print(f'{'+'*40}\n{"Simulador Bancário Versão 3.2":^38}\n{'+'*40}')
 menu="""
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
 return input(textwrap.dedent(menu)).upper()
# A linha de return solicita uma entrada para o usuário e aguarda a entrada do usuário.
# A entrada é atribuida a variavel nomeada 
# A função depositar recebe três parâmetros lembrando que o '/' indica que os 2 primeiros valores são posicionais e não são palavras-chaves;
# Lembrando que argumentos posicionais são passados com base na ordem em que são definidos na assinatura da função.
def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso.')
    else:
        print('Operação falhou.')
    return saldo, extrato # A função retorna uma tupla contendo o saldo e extrato atualizado da conta
# O asterisco na função 'sacar' indica que todos os argumentos após ele devem ser passados como palavra-chave ao chamar a função.
def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print('A operação falhou. Não tem saldo suficiente.')
    elif excedeu_limite:
        print('A operação falhou. Saque maior que o limite.')
    elif excedeu_saques:
        print('A operação falhou. Limite de saques excedido.')
    elif valor > 0:
        saldo = saldo - valor
        extrato = extrato + f'Saque: R$ {valor:.2f}'
        numero_saques = numero_saques + 1
        print('Saque realizado com sucesso' )
    else:
        print('Operação falhou. Valor informado inválido.')
    return saldo, extrato
# Parâmetros antes de '/' são posicionais; Após o '*'-asterisco- argumentos devem ser fornecidos como argumentos nomeados
def exibir_extrato(saldo,/,*,extrato):
     print(f'{"="*50}\n{"Extrato":^48}\n{"="*50}')
     print('Não foram realizadas movimentações.'if not extrato else extrato)
     print(f'Saldo: R$ {saldo:.2f}')
     print('='*50)

def main():
    limite_saques = 3  # Constante
    saldo = 0
    limite = 1000
    extrato = '' #Vazio
    numero_saques = 0
    while True:
        opcao = menu()
        if opcao == 'D':
            valor = float(input('Informe o valor do depósito: '))
            saldo,extrato = depositar(saldo,valor,extrato)
        elif opcao == 'S':
            valor = float(input('Informe o valor de saque: '))
            saldo,extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques,)
        elif opcao == 'E':
            exibir_extrato(saldo,extrato=extrato)
        elif opcao == 'Q':
            break
        else:
            print('Operacao invalida.')

main()            
                
