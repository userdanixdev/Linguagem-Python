# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Versão 02:

print('Locação de carros')
nome=input('Insira o nome do locador: ')
dia=int(input('Qual dia em que o carro foi alugado? '))
mes=input('Qual o mês em que foi alugado? ').capitalize()
dias=int(input('Quantos dais o carro foi alugado? '))
km=int(input('Quantos km ele foi rodado? '))
pagamento=(dias*60)+(km*0.15)
print()
print(f'O total a pagar é de {pagamento} reais.\nO carro foi alugado no dia {dia} e no mês {mes}\n.O nome do locador é:{nome}.')









