#Faça um programa que tenha uma função chamada escreva(), que receba um texto
#qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#Versão 07:
def linhas(txt):
    x=len(txt)+2
    print('><'*x)
    print(f'{txt.center(x)}')
    print('><'*x)

while True:
    frase=str(input('Insira sua frase: ')).capitalize()
    linhas(frase)
    resp=(input('Quer continuar?[S/N]: ')).strip().upper()
    if resp == 'N':
        break
