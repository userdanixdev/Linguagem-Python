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

print('+'*60)
sleep(1)
print('Tabela do campeonato brasileiro de futebol.')
print('+'*60)
sleep(1)
for t in times:
    print(t)
    sleep(0.5)
print('\nOs 5 primeiros colocados: ')
for time in range(0,len(times)):
    if time <= 4:
        print(f'{time +1}º{times[time]}.')
    else:
        print('+'*15)
        break
    sleep(1)
print('\nOs 4 últimos colocados: ')

for c in range(-4,len(times)):
    print(f'{times[c]}.' if c!=0 or c != None else print('+'*60))
    if c == 0:
        break
    sleep(1)
print('+'*60)
sleep(1)
print('Lista com os times em ordem alfabética: ')
for ordem in sorted(times):
    sleep(0.5)
    print(ordem)
print('+'*60)
sleep(1)
while True:
    clube=input('Digite o nome do seu time: ')
    if clube in times:
        print(f'O {clube} está na posição {times.index(clube)+ 1}º')
        break
    else:
        print('O seu time não está na lista.')
