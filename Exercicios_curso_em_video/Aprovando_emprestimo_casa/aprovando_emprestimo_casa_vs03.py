# Aprovando empréstimo:

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
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
