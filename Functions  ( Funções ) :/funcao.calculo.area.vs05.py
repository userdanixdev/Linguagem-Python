#Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.


# Versão 05:
# Valores de entrada 'inputs' dentro dos parâmetros da função:
def area(l,c):
    print(f'Um terreno de {l} X {c} tem uma área de {l*c:.2f}m².')
area(float(input('Largura(m):')),float(input('Comprimento(m): ')))
