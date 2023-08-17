
#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Aprovador de empréstimos em Python.')
valor_casa=float(input('Me informe o valor da casa: '))
salario_base=float(input('Me informe o seu salário: '))
anos=int(input('Quantos anos de pagamento? '))
salario_30=salario_base * 30/100
prestacao_mensal = valor_casa/(anos*12)
print(f'''
Com o valor da casa de R${valor_casa} reais em {anos} anos
a prestação será de R${prestacao_mensal:.2f} reais.
      ''')

if prestacao_mensal>=salario_30:
            print('Sendo assim, seu empréstimo será negado.')
else:
        print('Empréstimo concedido.')

Results:

Aprovador de empréstimos em Python.
Me informe o valor da casa: 120000
Me informe o seu salário: 5000
Quantos anos de pagamento? 10

Com o valor da casa de R$120000.0 reais em 10 anos
a prestação será de R$1000.00 reais.
      
Empréstimo concedido.

Result 02 com emprestimo NEGADO:

Aprovador de empréstimos em Python.
Me informe o valor da casa: 120000
Me informe o seu salário: 1000
Quantos anos de pagamento? 10

Com o valor da casa de R$120000.0 reais em 10 anos
a prestação será de R$1000.00 reais.
      
Sendo assim, seu empréstimo será negado.
=========================================================
