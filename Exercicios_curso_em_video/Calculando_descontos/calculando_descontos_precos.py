# Calculando Descontos nos Preços:

print('Desconto de 5%')
preco = float(input('Qual é o preço do produto? R$ '))
novo_preco = preco - (preco * 5/100)
print(f'O produto que custava R${preco}, na promoção de 5% vai custar R$ {novo_preco}.')
print()
print('Calculando Descontos:')
while True:
    price=float(input('Qual o preço do produto? '))
    desconto_x = int(input('De quanto será o desconto? '))
    desconto = (price/100)*desconto_x
    valor_final = price - desconto
    print(f'O produto que custava R${price:.2f} com {desconto_x:.0f}% de desconto vai custar R${valor_final:.2f}. ')
    saida = input('Fazer outra operação? 1-Sim / 2-Não: ')
    if saida == '1':
        continue
    elif saida == '2':
        break
print('Fim')

