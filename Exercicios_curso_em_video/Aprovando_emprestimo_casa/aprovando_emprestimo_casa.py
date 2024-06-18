# Aprovando empréstimo:

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Versão 01:

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12)
minimo=salario * 30/100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos. ')
print(f'a prestação será de R${prestacao:.2f}.')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO')

# Versão 02:

print()
print('Aprovador de emprestimo, vs1.1')
# inserção de dados:
pay = int(input('QUal o salario? R$'))
valor_casa = int(input('Qual o valor da casa que quer financiar? R$'))
tempo=int(input('Em quantos anos vai pagar? '))
# calculos:
pay_30=salario*0.3
total_juros=valor_casa*(1+0.03)**tempo
prestacao=total_juros/(tempo*12)
# condições:
if pay_30>=prestacao:
    print('financiamento aprovado')
    print(f'Voce ira pagar R${prestacao:.2f} por mês.')
    print(f'Total do financiamento: R$ {total_juros:.2f}')
else:
    print('Financiamento não aprovado, mensalidade superior a 30% do salario.')
print('fim')

# Versão 03:

print()
print('versao 03')
casa_=int(input('Qual será o valor da casa? '))
pay_=int(input('QUal será o salario? '))
ano_=int(input('Qunatos anos dispostos a pagar? '))      
prestacao_=casa_/(ano_*12)
if prestacao_ > pay_*0.3:
      print('Seu emprestimo foi negado.')
elif prestacao_ < pay_*0.3:
    print('Seu emprestimo foi aprovado.')

print(f'Para financiar uma casa de R${casa_:.2f}em {ano_} anos..')
print(f'A prestacao sera de R$ {prestacao_:.2f}')


