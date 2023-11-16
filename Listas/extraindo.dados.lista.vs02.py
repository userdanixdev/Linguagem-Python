
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

Resultado:

Digite um valor: 55
Quer continuar?[S/N]s
Digite um valor: 32
Quer continuar?[S/N]y
Resposta inválida. Quer continuar?[S/N]y
Resposta inválida. Quer continuar?[S/N]l
Resposta inválida. Quer continuar?[S/N]s
Digite um valor: 2
Quer continuar?[S/N]s
Digite um valor: 5
Quer continuar?[S/N]s
Digite um valor: 15
Quer continuar?[S/N]s
Digite um valor: 25
Quer continuar?[S/N]n
Vc digitou 6 elementos.
 Em ordem decrescente são [55, 32, 25, 15, 5, 2].
O valor 5 faz parte da lista.
 =======================================================
 
