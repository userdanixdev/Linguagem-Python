'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time de coração.'''

from time import sleep
times=('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo',
       'Vasco','Chapecoense','Atlético-MG','Botafogo','Atlético-PR','Bahia',
       'São Paulo','Fluminense','Sport','Vitória','Coritiba','Avaí','Ponte Preta',
       'Atlético-GO')
print(f'{"="*50}\n{"Tabela do Brasileirão":^48}{"="}\n{"="*50}')
sleep(1)
print('A tabela completa: ')
for c in range (0,20):
    sleep(0.3)
    print(f'{c+1}°{times[c]}')
print("="*50)
sleep(0.3)
while True:
    opcao= ' '
    while opcao not in '1234':
        opcao=(input('''
Escolha uma das opções abaixo:
[1] - Somente os 5 Primeiros colocados da tabela
[2] - Somente os 4 últimos colocados da tabela
[3] - Lista com os times em ordem alfabética
[4] - Posição do seu time de coração 
'''))
    sleep(0.3)
    print("="*50)
    if opcao == '1':
        print('\nOs 5 primeiros são: ')
        for c in range(0,len(times)-15):
            print(f'{c+1}°{times[c]}')
            sleep(0.3)
    print("="*50)
    sleep(0.5)
    
    if opcao == '2':        
        print('Os 4 últimos são: ')
        for pos,c in enumerate(times[16:]):
            pos = pos + 17
            print(f'{pos}° {c}')
            sleep(0.2)
    print('='*50)
    if opcao == '3':
        print('Times em ordem alfabética: ')
        for c in sorted(times):
            print(f'{times.index(c)+1}°{c}')
            sleep(0.5)
    print('+'*50)        
    if opcao == '4':
        clube=input('Digite o nome do seu time: ')
        if clube in times:
                 print(f'O {clube} está na posição {times.index(clube)+1}°')
        else:
            print('Seu time não está na lista.')
            sleep(0.3)
    sair = ' '
    while sair not in 'SN':
        sair =input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if sair == 'N':
        break
print('Encerrando...')
sleep(1)
print('Obrigado por tudo e fique ligado nas novidades do Camp.Brasileiro.')

               Resultados:

==================================================
             Tabela do Brasileirão              =
==================================================
A tabela completa: 
1°Corinthians
2°Palmeiras
3°Santos
4°Grêmio
5°Cruzeiro
6°Flamengo
7°Vasco
8°Chapecoense
9°Atlético-MG
10°Botafogo
11°Atlético-PR
12°Bahia
13°São Paulo
14°Fluminense
15°Sport
16°Vitória
17°Coritiba
18°Avaí
19°Ponte Preta
20°Atlético-GO
==================================================

Escolha uma das opções abaixo:
[1] - Somente os 5 Primeiros colocados da tabela
[2] - Somente os 4 últimos colocados da tabela
[3] - Lista com os times em ordem alfabética
[4] - Posição do seu time de coração 
3
==================================================
==================================================
==================================================
Times em ordem alfabética: 
20°Atlético-GO
9°Atlético-MG
11°Atlético-PR
18°Avaí
12°Bahia
10°Botafogo
8°Chapecoense
1°Corinthians
17°Coritiba
5°Cruzeiro
6°Flamengo
14°Fluminense
4°Grêmio
2°Palmeiras
19°Ponte Preta
3°Santos
15°Sport
13°São Paulo
7°Vasco
16°Vitória
++++++++++++++++++++++++++++++++++++++++++++++++++
Deseja continuar? [S/N]: s

Escolha uma das opções abaixo:
[1] - Somente os 5 Primeiros colocados da tabela
[2] - Somente os 4 últimos colocados da tabela
[3] - Lista com os times em ordem alfabética
[4] - Posição do seu time de coração 
2
==================================================
==================================================
Os 4 últimos são: 
17° Coritiba
18° Avaí
19° Ponte Preta
20° Atlético-GO
==================================================
++++++++++++++++++++++++++++++++++++++++++++++++++
Deseja continuar? [S/N]: n
Encerrando...
Obrigado por tudo e fique ligado nas novidades do Camp.Brasileiro.












        
