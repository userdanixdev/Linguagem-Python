# Gerenciador de pagamentos :
# Versão 04:
            
print('Gerenciador de pagamentos: Versão 02')
valor_produto = float(input('Digite o valor a ser pago: '))
opcoes=int(input('''
 Escolha um prazo de pagamento:
 
           [1] - A vista
           [2] - A vista no cartão
           [3] - Em até 2x no cartão
           [4] - 3x ou mais
           
 Digite o valor correspondente a forma de pagamento: '''))

vista=int(1)
cartao=int(2)
duas_vezes=int(3)
tres_vezes=int(4)

if opcoes == vista:
    desconto = valor_produto * 0.90
    print(f'A compra será realizada com desconto de 10%, ficando assim no valor de R${desconto:.2f}')
elif opcoes == cartao:
    desconto = valor_produto * 0.95
    print(f'A compra será realizada com desconto de 5%, ficando no valor de R${desconto:.2f}')
elif opcoes == duas_vezes:
    valor_parcelado = valor_produto/2
    print(f'A compra será realizada em duas parcelas no valor de R${valor_parcelado:.2f} sm juros.')
elif opcoes == tres_vezes:
    numero_parcelas=int(input('Digite o número de parcelas: '))
    if numero_parcelas < 3:
        print('Numero inválido. Insira um valor válido.')
    else:
        valor_juros = valor_produto*1.2
        valor_parcelas_com_juros = valor_juros / numero_parcelas
        print(f'''
            A compra será realizada em {numero_parcelas} parcelas,com juros de 20%.
              A novo valor do produto com juros será de R${valor_juros:.2f}.
              Os valores das parcelas serão de R${valor_parcelas_com_juros:.2f}''')
else:
    print('Escolha inválida. Por favor, escolha a opção válida.')
