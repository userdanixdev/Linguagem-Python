#Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.


# Versão 02:
def area(a,b):
    return a*b

# Programa principal:
x= float(input('Digite a largura: '))
y= float(input('Digite o comprimento: '))
terreno = area(x,y)
print(f'A área total é de {terreno}m².')
