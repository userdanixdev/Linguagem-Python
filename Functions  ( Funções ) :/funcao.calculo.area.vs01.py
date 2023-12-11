#Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.


# Versão 02:
def metros2(a,b):
    print(f'A área de um terreno com {a} & {b} é de {a*b}m².')

# Programa principal:
print('-'*40)
print(f'{"Controle de terrenos":^40}')
print('-'*30)
l=float(input('Largura do terreno em metros: '))
c=float(input('Comprimento do terreno em metros: '))
metros2(l,c)
print('FIM')
    
