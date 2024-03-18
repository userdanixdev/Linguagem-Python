'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

# Versão 02:

times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')
from time import sleep
print('+'*80)
sleep(1)
print('Tabela do Brasileirão 2023')
print('+'*80)
sleep(1)
for t in times:
  print(t)
  sleep(0.3)
print('\n Os 5 primeiros colocados do Brasileirão 2023: ')
for time in range(0,len(times)):
  if time <= 4:
      print(f'{time+1}º{times[time]}.')
  else:
    print('+'*30)
    break
  sleep(1)    
print('\n Os 4 últimos colocados do Brasileirão 2023: ')
for c in range(-4,len(times)):
  print(f'{times[c]}.' if c != 0 or c != None else print('+'*15))
  if c == 0:
    break
  sleep(1)
print('+'*50)
sleep(0.7)
print('Lista dos times em ordem alfabética: ')
for ordem in sorted(times):
  sleep(0.5)
  print(ordem)
print('='*15)
sleep(1)
while True:
  clube=input('Digite o nome do seu time: ').capitalize()
  if clube in times:
    print(f'O {clube} está na posição {times.index(clube}+1}º')
    break
  else:
    print('O seu time não está na lista.')
