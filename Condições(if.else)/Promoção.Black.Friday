#Na última black friday, o gerente de uma loja de perfumes colocou todo o seu
#estoque em promoção.
#Construa um programa que solicite o preço e a forma de pagamento que:
#ao fim deve informar o valor final a ser pago.

print('''
                - PROMOÇÃO BLACK FRIDAY -
               TODOS OS ESTOQUES EM PROMOÇÃO
                      - PERFUMES -
  ===========================================================
            1. À vista(em espécie) - 15% de desconto
            2. Cartão de débito    - 10% de desconto
            3. Cartão de crédito   -  5% de desconto
            =========================================
            ''')

valor=float(input('Digite o valor a ser pago R$: '))
opcao= int(input('Escolha a forma de pagamento: '))

if opcao<1 or opcao>3:
    print('Forma de pagamento inválida.')
elif opcao == 1:
    valor_final=valor*0.15
    print(f'Valor a pagar a vista com desconto será R${valor-valor_final}reais.')
elif opcao == 2:
    valor_final = valor*0.10
    print(f'Valor a pagar no cartão de débito será de R$ {valor-valor_final} reais.')
else:
    valor_final = valor*0.05
    print(f'Valor no cartão de crédito será de R$ {valor-valor_final} reais.')

Result:

  - PROMOÇÃO BLACK FRIDAY -
               TODOS OS ESTOQUES EM PROMOÇÃO
                      - PERFUMES -
  ===========================================================
            1. À vista(em espécie) - 15% de desconto
            2. Cartão de débito    - 10% de desconto
            3. Cartão de crédito   -  5% de desconto
            =========================================
            
Digite o valor a ser pago R$: 250
Escolha a forma de pagamento: 2
Valor a pagar no cartão de débito será de R$ 225.0 reais.
========================================================================
            
    

