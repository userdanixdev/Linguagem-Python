# Tabela do Brasileiro 2023 :
# Versão 05: com laço for e range

times=('Palmeiras','Atlético-MG','Flamengo','Grêmio','Botafogo',
       'RB Bragantino','Fluminense','Athletico','São Paulo',
       'Cuiabá','Corinthians','Cruzeiro','Santos','Vasco','Bahia','Goiás',
       'Coritiba','América-MG','Atlético-GO','Fortaleza')

print('Campeonato Brasileiro 2023')
print('Tabela completa:\n')
for contagem in range(0,len(times)):
    print(f'{contagem+1}º{times[contagem]}.')
print('\nOs 5 primeiros colocados:\n')
for contagem in range(0,5):
    print(f'{contagem+1}º{times[contagem]}.')
print('\nOs 4 últimos colocados:\n')
for contagem in range(16,len(times)):
    print(f'{contagem+1}º{times[contagem]}')
print('\nTabela em ordem alfabética:\n')
for contagem in range(0,len(times)):
    print(f'{contagem+1}-{sorted(times)[contagem]}.')
    
    
              
        
