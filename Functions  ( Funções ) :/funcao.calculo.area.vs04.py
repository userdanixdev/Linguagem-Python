#Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.


# Versão 04:
def area():
    l=float(input('Digite a largura do seu terreno: '))
    c=float(input('Digite o comprimento do seu terreno: '))
    area=l*c
    print(f'Seu terreno tem {area:.2f}M² de área.')


area()
