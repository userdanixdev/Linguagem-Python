
# EXTRAINDO DADOS DA UMA LISTA

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
 #   A) Quantos números foram digitados.
 #   B) A lista de valores, ordenada de forma decrescente.
 #   C) Se o valor 5 foi digitado e está ou não na lista.

 # Versão 04 #

lista=list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar?[S/N]').strip().upper()[0]   # Irá fazer com que o usuário digite a letra correta infinitamente
    while resp not in 'SsNn':
        resp = input('Quer continuar?[S/N]').strip().upper()[0]  # Irá fazer com que o usuário digite a letra correta infinitamente
    if resp in 'nN':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte desta lista.')

Resultado:

Digite um valor: 5
Quer continuar?[S/N]r
Quer continuar? [S/N].r
Quer continuar? [S/N].s
Digite um valor: 65
Quer continuar?[S/N]t
Quer continuar? [S/N].s
Digite um valor: 1
Quer continuar?[S/N]s
Digite um valor: 32
Quer continuar?[S/N]n
Vc digitou 4 elementos.
Os valores em ordem decrescente são [65, 32, 5, 1].
O valor 5 faz parte da lista.

