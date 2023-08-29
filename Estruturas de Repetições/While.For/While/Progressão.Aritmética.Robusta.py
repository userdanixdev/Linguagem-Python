#Lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''Tem o mesmo exercício na pasta de estrutura de repetição na pasta 'FOR' '''
'''Este será feito com a estrutura 'WHILE' '''

# Progressão Aritmética ROBUSTA #

print('Gerador de Progressão Aritmética')
primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro
cont=1
total=0
mais=10  # valor da variável a partir de 10
while mais !=0:  # 2ºpasso: criar outra estrutura de repetição fora do bloco.
    total = total + mais
    while cont<=total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont =  cont + 1
    print('PAUSA')
    mais = int(input('Quantos termo você quer mostrar a mais? ')) #1°passo: criar uma variável
print(f'Progressão finalizada com {total} termos mostrados.')
print('FIm')

Results:
Gerador de Progressão Aritmética
Primeiro termo: 2
Razão da PA: ,2
2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> 16 -> 18 -> 20 -> PAUSA
Quantos termo você quer mostrar a mais? 2
22 -> 24 -> PAUSA
Quantos termo você quer mostrar a mais? 0
Progressão finalizada com 12 termos mostrados.
FIm
======================================================


