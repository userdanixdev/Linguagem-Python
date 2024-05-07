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

# A função 'sleep' do módulo 'time' usado para pausar a execucação do programa para um determinado tempo
from time import sleep 
print('+'*40)
sleep(1) # Irá pausar por 1 segundo
# Para centralizar o título use a função f-strings, com aspas duplas para o título princiapl seguido de :^40 para centralizar
print(f'{"Tabela do Brasileirão 2023":^40}') 
print('+'*40)
sleep(1)
 # A variável de execução 't' irá iterar sobre cada elemento de 'times' e com o print, mostrar na tela cada valor da tupla.
 # Com a iteração, a impressão irá sair de maneira mais clean, uma embaixo da outra.
for t in times: 
    print(t)
    sleep(0.3)
print('Os 5 primeiros colocados do Brasileirão 2023: ')
for time in range(0,len(times)): # O range é um comprimento definido de 0 até o comprimento total da tupla 'times'.
    if time <= 4:
        print(f'{time+1}º{times[time]}.') # Se time for <= a 4 recebe a posição + 1 e em seguida o nome do time.
    else:
        print('+'*30)
        break
    sleep(0.5)
print('os 4 últimos colocados do Brasileirão 2023: ')
for time in range(-4,len(times)):
    print(f'{times[time]}.' if time != 0 or time != None else print('+'*15))
    if time == 0:
        break
    sleep(0.7)
print('+'*50)
sleep(0.7)
print('Lista dos times em ordem alfabética: ')
for ordem in sorted(times):  # Função sorted irá colocar a tupla em ordem alfabética
    sleep(0.5)
    print(ordem)
print('+'*15)
sleep(1)

for ordem in range(0,len(times)):  
    sleep(0.5)
    print(f'{ordem+1}º{sorted(times)[ordem]}.') # colocar o sorted aqui
print('+'*15)
sleep(1)
while True:
    clube = input('Digite o nome do seu time: ').capitalize()
    if clube in times:
        print(f'O {clube} está na posição {times.index(clube}+1°')
        break
    else:
        print('O seu time não está na lista.')
    
