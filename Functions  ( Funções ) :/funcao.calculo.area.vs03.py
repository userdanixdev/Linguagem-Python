#Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.


# Versão 03:
# Versão interessante com o processo inteiro em um só bloco na função:
def area():
    while True:
        a=float(input('Qual o valor de uma dimensão? '))
        b=float(input('Qual o valor da outra dimensão? '))
        area=a*b
        print(f'O valor da área de um terreno com {a} metros de largura e\n {b} metros de comprimento é: {area} m².')
        opcao = str(input('Quer continuar?[S/N]')).strip().upper()[0]
        while opcao not in "SsNn":
            opcao = input('Quer continuar?[S/N]')
        if opcao in 'Nn':
            print('FIM DO PROGRAMA')
            break
     
area()
