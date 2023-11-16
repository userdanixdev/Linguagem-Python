
# EXTRAINDO DADOS DA UMA LISTA

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
 #   A) Quantos números foram digitados.
 #   B) A lista de valores, ordenada de forma decrescente.
 #   C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
while True:    # loop while para vários números
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print(f'Vc digitou {len(valores)} elementos.')
#valores.sort()  # irá botar na ordem CRESCENTE
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:   # in faz pesquisa dentro de listas e tuplas, não precisa de loop, valor específico.
    print('O valor 5 faz parte da lista!.')
else:
    print('O valor 5 não foi encontrado na lista.')

REsultado:
Digite o núnmero: 15
Quer continuar? [S/N] s
Digite o núnmero: 2
Quer continuar? [S/N] s
Digite o núnmero: 30
Quer continuar? [S/N] s
Digite o núnmero: 22
Quer continuar? [S/N] n
Vc digitou 4 elementos.
Os valores em ordem decrescente são [30, 22, 15, 2].
O valor não foi encontrado na lista.

 

 

 
