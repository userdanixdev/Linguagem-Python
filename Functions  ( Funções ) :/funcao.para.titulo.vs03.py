#Faça um programa que tenha uma função chamada escreva(), que receba um texto
#qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Títulos como função - versão 03:

def titulo(txt):
    print(f'{"~"*(len(txt)+4)}\n{txt:^{(len(txt)+4)}}\n{"~"*(len(txt)+4)}')
titulo(input('Escreva uma mensagem: '))    

