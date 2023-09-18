'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

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
print('\nOs 5 primeiros são: ')
for c in range(0,len(times)-15):
    sleep(0.3)
    print(f'{c+1}°{times[c]}')
print("="*50)
sleep(0.3)
print('Os 4 últimos são: ')
for pos,c in enumerate(times[16:]):
    pos = pos + 17
    print(f'{pos}° {c}')
    sleep(0.2)
print('='*50)
print('Times em ordem alfabética: ')
for c in sorted(times):
       print(f'{times.index(c)+1}°{c}')
print('+'*50)
sleep(1)
while True:
    clube=input('Digite o nome do seu time: ')
    if clube in times:
        print(f'O {clube} está na posição {times.index(clube)+1}°')
        break
    else:
        print('Seu time não está na lista.')

