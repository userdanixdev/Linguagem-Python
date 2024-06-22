# Desafio:
# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, 
# à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
# Entrada :
# A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste.
# Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.
# Saída: Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
n = int(input())

while(n > 0):
  values =input().split()
  aux=''
  for digit in values[0][::-1]:  #<- Inverte a primeira string de 'values'
    aux += digit # <- 'aux' recebe os valores invertidos
    # Verificação de encaixe:
    if aux == values[1][::-1]:  # Verifica se 'aux' é igual a string [1] a da direita.
      print('encaixa')
      break
    else:    
     print('não encaixa')
    
aux=''
n -=1    
    
    ''' 
    TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
    "encaixa" ou "não encaixa" para cada uma das relações N vezes.
    '''

'''Explicação:

Para a primeira entrada 56789 6789, a segunda string 6789 é um sufixo da primeira string, então encaixa.
Para a segunda entrada 12345 543, a segunda string 543 não é um sufixo da primeira string, então nao encaixa.
O código usa [::-1] para inverter strings e, assim, facilita a verificação de sufixos de uma maneira incremental e comparativa.'''
