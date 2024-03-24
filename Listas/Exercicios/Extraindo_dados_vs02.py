# EXTRAINDO DADOS DA UMA LISTA

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
 #   A) Quantos números foram digitados.
 #   B) A lista de valores, ordenada de forma decrescente.
 #   C) Se o valor 5 foi digitado e está ou não na lista.

### VERSÃO 02: ###

valores=[]
while True:
    valores.append(int(input('Digite um valor: ')))
    pergunta=input('Quer continuar? [S/N]: ')
    while pergunta not in 'sSnN':
        pergunta=input('Resposta inválida. Quer continuar? [S/N]: ')
    if pergunta in 'Nn':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Em ordem decrescente são {valores}.')
if 5 not in valores:
    print('O valor 5 não está na lista.')
else:
    print('O valor 5 está na lista.')
