# Aprovando empréstimo:

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
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
