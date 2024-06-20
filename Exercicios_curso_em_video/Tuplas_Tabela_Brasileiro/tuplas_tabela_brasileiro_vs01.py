# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Fortaleza.

# Tabela do Brasileiro 2023 :
# Versão 01 :

from time import sleep

times=('Palmeiras','Atlético-MG','Flamengo','Grêmio','Botafogo',
       'RB Bragantino','Fluminense','Athletico','São Paulo',
       'Cuiabá','Corinthians','Cruzeiro','Santos','Vasco','Bahia','Goiás',
       'Coritiba','América-MG','Atlético-GO','Fortaleza')

print('Tabela do Brasileirão 2023')
sleep(2)
print(f'\nLista de times: {times}')
sleep(1)
print('\nLista formatada: \n')
for t in times:
    sleep(0.3)
    print(t)
sleep(1)    
print(f'\nOs 5 primeiros são:\n {times[0:5]}')
sleep(1)
print(f'\nOs 4 últimos são:\n {times[-4:]}.')
sleep(1)
print()
print(f'Os times em ordem alfabética:\n {sorted(times)}.')
sleep(1)
print()
print(f'O Fortaleza está na {times.index("Fortaleza")+1}º posição.')
sleep(1)
print('\nFim')
