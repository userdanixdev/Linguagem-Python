#Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a área do terreno.


## Função área:
def area(l,c):
    a = l * c
    print(f'A área de um terreno com {l} & {c} é de {a}metros.')

# Programa principal:
print('Controle de terreos: ')
print('-'*30)
l=float(input('Largura em metros: '))
c=float(input('Comprimento em metros: '))
area(l,c)
    
