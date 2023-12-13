#Faça um programa que tenha uma função chamada escreva(), que receba um texto
#qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#Função para títulos:

def escreva(titulo):
    tam=len(titulo) + 4 #<--- len é o tamanho da mensagem. 'O +4 para ficar uma borda.'
    print('+'*tam)
    print(f'  {titulo}')   ## Dois espaços na função para centralizar o título.
    print('+'*tam)

escreva('Olá, mundo.')
escreva('Curso de Python no Youtube.')
## AS LINHAS IRÃO ACOMPANHAR O TÍTULO ##
escreva('Chega disso!')
    

    


