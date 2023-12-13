#Faça um programa que tenha uma função chamada escreva(), que receba um texto
#qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Títulos como função - versão 04:
# Aqui o símbolo é definido para GERAR AS LINHAS. Duas varíáveis contínuas:

def titulo(simb,txt):
    tam=len(txt)+4
    print(simb*tam)
    print(f'{txt:^{tam*len(simb)}}')
    print(simb*tam)

# Programa Principal:
titulo('><','Programa Python para todos')

