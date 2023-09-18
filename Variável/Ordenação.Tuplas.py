'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times=('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo',
       'Vasco','Chapecoense','Atlético-MG','Botafogo','Atlético-PR','Bahia',
       'São Paulo','Fluminense','Sport','Vitória','Coritiba','Avaí','Ponte Preta',
       'Atlético-GO')
#print(f'Lista de times: {times}')  Sem formatação
for t in times:
    print(t)

# Os cinco primeiros colocados:
print('+'*60)
print(f' Os 5 primeiros times do Brasileirão: {times[0:5]}.')
print('+'*60)
# Os quatro últimos colocados:
print('+'*60)
print(f'Os 4 últimos são: {times[-4:]}')
print('+'*60)
# Times em ordem alfabética:
print('+'*60)
print(f'Os times na ordem alfabética: {sorted(times)}')
print('+'*60)
#Em que posição está o time da CHAPECOENSE:
print('+'*60)
print(f' O time da CHAPECOENSE está na {times.index("Chapecoense")+1}ª posição.')
print('+'*60)



