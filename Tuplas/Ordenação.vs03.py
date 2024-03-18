'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

from time import sleep
times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

print(f'{"="*50}\n{"Tabela do Brasileirão 2023":^48}{"="}\n{"="*50}')
sleep(1)
print(' '*20)
for c in range(0,20):
  sleep(0.5)
  print(f'{c+1}°{times[c]}')
print('='*20)  
print('\nOs 5 primeiros colocados da tabela são: ')
for c in range(0,len(times)-15):
    sleep(0.3)
  print(f'{c+1}°{times[c]}')
print(' '*20)  
sleep(1.5)
print('Os 4 últimos colocados são:')
for pos,c in enumerate(times[16:]):
    pos = pos + 17
    print(f'\n{pos}º{c}')
    sleep(0.3)
print(' '*15)
print('Times em ordem alfabética: ')
for c in sorted(times):
  sleep(0.3)
  print(f'{c}')
print('='*15)
sleep(1)
  
