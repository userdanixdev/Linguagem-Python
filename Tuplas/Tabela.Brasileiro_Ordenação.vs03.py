'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

clubes=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

# A função 'sleep' do módulo 'time' usado para pausar a execucação do programa para um determinado tempo
from time import sleep 
sleep(1) # Irá pausar por 1 segundo
# Para centralizar o título use a função f-strings, com aspas duplas para o título princiapl seguido de :^40 para centralizar
print(f'{"="*50}\n{"Tabela do Brasileirão 2023":^48}{"="}\n{"="*50}')
sleep(1)
 # A variável de execução 't' irá iterar sobre cada elemento de 'times' e com o print, mostrar na tela cada valor da tupla.
 # Com a iteração, a impressão irá sair de maneira mais clean, uma embaixo da outra.
for t in range(0,20): 
    print(f'{t+1}º{clubes[t]}')
    sleep(0.3)
print(' '*20)    
print('Os 5 primeiros colocados do Brasileirão 2023: \n')
for t in range(0,len(clubes)-15): # O range é um comprimento definido de 0 até o comprimento total da tupla 'times'.
    sleep(0.3)
    print(f'{t+1}º{clubes[t]}')
print(' '*20)
sleep(1)
print('Os 4 últimos colocados são: ')
# a função enumerate irá retornar tanto o indice quanto o valor do elemento em uma sequencia
for indice,valor in enumerate(clubes[16:]):
    sleep(0.3)
    indice = indice + 17 # Estamos começando a enumeração a partir do indice 16. adicionar 17 a cada iteração.
    print(f'{indice}º{valor}')
print(' '*15)
print('Times em ordem alfabética: \n')
for t in sorted(clubes):
    sleep(0.3)
    print(f'{t}')
print(' '*15)
sleep(1)
print('Times em ordem alfabética ordenada por posição: \n')
for ordem in range(0,len(clubes)):
    print(f'{ordem+1}º{sorted(clubes)[ordem]}')
    sleep(0.3)
print('\nFim')    
    


  
