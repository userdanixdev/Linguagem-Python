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

O resultado desse código deverá ser este:

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Tabela do campeonato brasileiro de futebol.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Corinthians
Palmeiras
Santos
Grêmio
Cruzeiro
Flamengo
Vasco
Chapecoense
Atlético-MG
Botafogo
Atlético-PR
Bahia
São Paulo
Fluminense
Sport
Vitória
Coritiba
Avaí
Ponte Preta
Atlético-GO

Os 5 primeiros colocados: 
1ºCorinthians.
2ºPalmeiras.
3ºSantos.
4ºGrêmio.
5ºCruzeiro.
+++++++++++++++

Os 4 últimos colocados: 
Coritiba.
Avaí.
Ponte Preta.
Atlético-GO.
Corinthians.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Lista com os times em ordem alfabética: 
Atlético-GO
Atlético-MG
Atlético-PR
Avaí
Bahia
Botafogo
Chapecoense
Corinthians
Coritiba
Cruzeiro
Flamengo
Fluminense
Grêmio
Palmeiras
Ponte Preta
Santos
Sport
São Paulo
Vasco
Vitória
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Digite o nome do seu time: Flamengo
O Flamengo está na posição 6º
