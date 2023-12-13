#Faça um programa que tenha uma função chamada escreva(), que receba um texto
#qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Títulos como função - versão 06:

def texto(txt):
    print('><'*(len(txt)+4))
    print(f'{txt:^{len(txt)+4}}')
    print('><'*(len(txt)+4))

while True:
    resp=input('Texto: ').strip()
    texto(resp)
    cont=str(input('Continuar?[S/N]: ')).strip().upper()[0]
    if cont not in 'SN':
        print('Resposta inválida.')
    if cont == 'N':
        break
print('<<<FIM>>>')    
    
