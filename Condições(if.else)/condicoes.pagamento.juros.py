

#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#– 1. à vista dinheiro/cheque: 10% de desconto
#– 2. à vista no cartão: 5% de desconto
#– 3. em até 2x no cartão: preço formal 
#– 4. 3x ou mais no cartão: 20% de juros

preço=float(input('Digite o preço do produto R$: '))
opçao=int(input('''
           Escolha a forma de pagamento:
            1. Para pagamento a vista ou no cheque: 10% de desconto
            2. Para pagamento a vista no cartão: 5% de desconto
            3. 2x no cartão de crédito: Preço normal
            4. 3x ou mais no cartão de crédito: 20% de juros
           '''))
if opçao <1 or opçao>4:
        print('Forma de pagamento inválida.')
elif opçao == 1:
    a_vista_cheque = preço - (preço*0.10)
    print(f'A vista ou no cheque o valor será de R$ {(a_vista_cheque)} reais.')
elif opçao == 2:
    a_vista_cartao = preço - (preço*0.05)
    print(f'A vista no cartão o valor do produto sairá por R${a_vista_cartao} reias.')
elif opçao == 3:
    duas_x_cartao= preço/2
    print(f'Em até 2x no cartão o produto terá seu valor inalterado e ficará em 2x de R${duas_x_cartao} reais.')
elif opçao == 4:
    preço_juros = preço + (preço*0.20)
    parcelas=int(input('Quantas parcelas? '))
    num_parcelas = preço_juros/parcelas    
    #tres_x_cartao= preço/3 + (preço*0.20)
    print(f'''
Em 3x no cartão de crédito ou mais o produto terá seu valor com juros de 20% ao mês.
O valor da compra de R${preço} reais em {parcelas} parcelas ficará no valor de R$:{num_parcelas:.2f} reais por mês.
Com um total de: R${preço_juros} reais.
''')
        
        
        






