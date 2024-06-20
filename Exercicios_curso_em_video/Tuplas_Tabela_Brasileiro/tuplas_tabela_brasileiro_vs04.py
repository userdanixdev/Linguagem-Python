# Tabela do Brasileiro 2023 :
# Versão 04: laço for com enumerate

times=('Palmeiras','Atlético-MG','Flamengo','Grêmio','Botafogo',
       'RB Bragantino','Fluminense','Athletico','São Paulo',
       'Cuiabá','Corinthians','Cruzeiro','Santos','Vasco','Bahia','Goiás',
       'Coritiba','América-MG','Atlético-GO','Fortaleza')

print('Campeonato Brasileiro 2023')
for posicao,time in enumerate(times):
    print(f'{posicao+1}º{time}.')
print('\nOs 5 primeiros colocados: ')    
for posicao,time in enumerate(times[0:5]):
    print(f'{posicao+1}º{time}.')
print('\nOs 4 últimos rebaixados: ')    
for posicao,time in enumerate(times[-4:]):
    print(f'{posicao+17}º{time}.')
print('\nClubes em ordem alfabética: ')
for posicao,time in enumerate(sorted(times)):
    print(f'{posicao+1}-{time}.')
clube=input('Digite o nome do clube: ').capitalize()
if clube in times:
    print(f'O time {clube} está na {times.index(clube)+1}º posição.')
    



        
              
        
