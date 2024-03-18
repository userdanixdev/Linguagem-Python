'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

for t in range(0,1):
  print(times)
print('='*60)
print(f'Os 5 primeiros times do Brasileirão 2023: {times[0:5]}')
print('='*60)
print(f'Os 4 últimos times do Brasileiro 2023: {times[-4:]}')
print('='*60)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('='*60)
print(f'O time do Vasco está na: {times.index("Vasco")+1} º posição.')




  
