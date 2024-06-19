# Gerenciador de pagamentos:
# Versão 1 

# Gerenciador de pagamento: Loja

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

# Versão 01:

print('Loja de roupas')
preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
        [1] - a vista - Dinheiro/cheque
        [2] - a vista cartão
        [3] - 2x no cartão
        [4] - 3x ou mais no cartão
        ''')
opcao=int(input('QUal a opção? '))
if opcao == 1:
    total = preco - (preco*10/100)
elif opcao == 2:
    total = preco - (preco*5/100)
    print(f'Sua compra de R$ {preco} vai custar R${total}.')
elif opcao == 3:
    total = preco
    parcela = total/2
    print(f'Sua compra parcelada  em 2x de {parcela}.')
elif opcao == 4:
    total = preco + (preco*20/100)
    total_parc=int(input('Quantas parcelas? '))
    parcela =  total / total_parc
    print(f'Sua compra será parcelada em {total_parc} de R$ {parcela} com juros.')
print(f'Sua compra de R${preco} vai custar {total} no final.')    
    
