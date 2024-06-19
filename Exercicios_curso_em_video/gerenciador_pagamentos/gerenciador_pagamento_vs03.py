# Gerenciador de pagamentos :
# Versão 03: Loop de validação de entrada de dados do preço das compras e looping para realizar novas compras.

while True:
    print('Loja de roupas')
    while True:
        try:
            preco = float(input('Preço das compras: R$ '))
            if preco > 0 and preco < 10000:
                break
            else:
                print('O preço deve ser maior que zero e no máximo R$ 10.000,00.')
        except ValueError:
            print('Entrada inválida. Por favor, insira um valor numérico.')
            
    while True:
        print('''  FORMAS DE PAGAMENTO
                [1] - à vista / Dinheiro
                [2] - à vista cartão
                [3] - 2x no cartão
                [4] - 3x ou mais no cartão
                ''')
        opcao = int(input('Qual a opção? '))
        if opcao == 1:
            total = preco-(preco*10/100)
            print(f'Sua compra de R${preco:.2f} vai custar R$ {total:.2f} com 10% de desconto.')
            break
        elif opcao == 2:
            total = preco - (preco*5/100)
            print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} com 5% de desconto.')
            break
        elif opcao == 3:
            total = preco
            parcela = total/2
            print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
            break
        elif opcao == 4:
            total_parc = int(input('Quantas parcelas? '))
            if total_parc <= 2:
                print('\nSelecione a opção 3 para parcelamento em até 2x sem juros.\n')
            else:
                total = preco + (preco*20/100)
                parcela = total/total_parc
                print(f'Sua compra será parcelada em {total_parc}x de R${parcela:.2f} com juros.')
                break
        else:
            print('Opção inválida. Tente novamente.')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
    while True:
        continuar = input('\nGostaria de realizar mais compras? [1-SIM / 2-NÃO] ')
        if continuar in ['1','2']:
            break
        else:
            print('Digite somente 1 para SIM e 2 para não.')
    if continuar == '2':
        break
print('Fim')        
            

            
