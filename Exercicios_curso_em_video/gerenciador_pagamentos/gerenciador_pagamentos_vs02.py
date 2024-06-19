# Gerenciador de pagamentos :
# Versão 02:

print('Loja de roupas')
preco = float(input('Preço das compras: R$ '))
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

            
