#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista=[1,2,3,4,5]
while True:
  n1=int(input('Digite um número: ')
         if n1 in lista:
         print('Digite valores que não estão na lista') 
         else:
           lista.append(n1)
        pergunta=input('Quer continuar? [S/N] ')
        if pergunta not in 'SsNn':
          pergunta=input('Resposta inválida. Somente S para sim e N para não. QUer continuar? [S/N] ')
        if pergunta in 'Nn':
          break
print('='*30)
print(f'Você digitou os valores {lista}.')
print(f'Os valores em ordem crescente são {sorted(lista)} ')


