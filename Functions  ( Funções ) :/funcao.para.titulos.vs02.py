#Faça um programa que tenha uma função chamada escreva(), que receba um texto
#qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#Títulos como função - versão 02:

def escreva(txt):
    t=len(txt)+4
    print('~'*t)
    print(f'{txt:^{t}}')
  # print('~'*t)

escreva('Batman = Arkham Prison')
escreva('Batman = Arkham City')
escreva('Batman = Arkham Knights')

