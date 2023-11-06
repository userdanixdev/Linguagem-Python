
# EXTRAINDO DADOS DA UMA LISTA

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
 #   A) Quantos números foram digitados.
 #   B) A lista de valores, ordenada de forma decrescente.
 #   C) Se o valor 5 foi digitado e está ou não na lista.

 # Versão 02 #

valores=[]
while True:
    valores.append(int(input('Digite um valor: ')))
    cont=input('Quer continuar? [S/N]')
    while cont not in 'SsNn':
        cont=input('Resposta não válida. Quer continuar?[S/N]')
    if cont in 'Nn':
        break
valores.sort(reverse=True)
print(f'Vc digitou {len(valores)} elementos.\n Em ordem decrescente são {valores}')
if 5 not in valores:
    print('O valor 5 não faz parte da lista.')
else:
    print('O valor 5 faz parte da lista.')
 
