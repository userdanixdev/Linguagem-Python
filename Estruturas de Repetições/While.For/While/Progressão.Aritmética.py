#Lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''Tem o mesmo exercício na pasta de estrutura de repetição na pasta 'FOR' '''
'''Este será feito com a estrutura 'WHILE' '''

print('Gerador de Progressão Aritmética')
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro
cont=1
while cont<=10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont =  cont + 1
print('FIM')    

Result:

Gerador de Progressão Aritmética
Primeiro termo: 0
Razão da PA: 5
0 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35 -> 40 -> 45 -> FIM



