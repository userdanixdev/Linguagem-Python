'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

# Criar uma tupla com os times do Brasileirão:
times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

print(times) # Com a função print, imprime toda a tupla.
print('='*60)
# O slicing [0:5] irá retornar uma sub-tupla contendo os elementos do índice 0 a 4 ( Os 5 primeiros )
print(f'Os 5 primeiros times do Brasileirão 2023: {times[0:5]}') 
print('='*60)
# O slicing [-4:] irá retornar uma sub-tupla contendo os 4 últimos elementos.
print(f'Os 4 últimos times do Brasileiro 2023: {times[-4:]}')
print('='*60)
# A função sorted() ordena os elementos da tupla em ordem alfabética.
print(f'Os times em ordem alfabética: {sorted(times)}')
print('='*60)
print(f'O time do Vasco está na: {times.index("Vasco")+1} º posição.')
# O método index() retorna o índice do elemento, em Python a contagem começa com 0.
# Portanto precisamos adicionar '+1' para obter a posição real dentro da tupla.



  
