# Tabela do Brasileiro 2023 :
# Versão 03:


times=('Palmeiras','Atlético-MG','Flamengo','Grêmio','Botafogo',
       'RB Bragantino','Fluminense','Athletico','São Paulo',
       'Cuiabá','Corinthians','Cruzeiro','Santos','Vasco','Bahia','Goiás',
       'Coritiba','América-MG','Atlético-GO','Fortaleza','Sport')

print(f'{"+"*40}\nA lista de times do Brasileirão 2023:\n{"+"*40}\n{times}.')
print(f'Os primeiros 5 colocados foram:\n{times[0:5]}\n')
print(f'Os times que vão para a fase de grupo da Libertadores:\n{times[0:6]}.\n')
print(f'Os dois times que vão para a pré-libertadores:\n{times[6:8]}.\n')
print(f'Os times da sul-americana são:\n {times[8:14]}.\n')
print(f'Os times rebaixados foram:\n{times[17:]}.\n')
print(f' Os times em ordem alfabética:\n{sorted(times)}.\n')
print(f' O fortaleza está na {times.index("Fortaleza")+1}º posição.')
print('Fim.')
        



        
              
        
