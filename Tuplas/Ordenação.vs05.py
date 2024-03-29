  '''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time de coração.'''

from time import sleep
times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

print(f'{"="*50}\n{"Tabela do Brasileirão 2023":^48}\n{"="*50}')
sleep(1)
print('Tabela completa: ')
for c in range (0,20):
  sleep(0.3)
  print(f'{c+1}°{times[c]}')
print('='*20)
sleep(0.3)
while True:
  opcao=' '
  while opcao not in '1234':
    opcao=input('''
Escolha uma das opções abaixo:
[1] - Somente os 5 Primeiros colocados da tabela
[2] - Somente os 4 últimos colocados da tabela
[3] - Lista com os times em ordem alfabética
[4] - Posição do seu time de coração 
''')
  sleep(1)
  print('='*20)
  if opcao == '1':
      print('\nOs 5 primeiros são: ')
      for c in range(0,len(times)-15):
        print(f'{c+1}º{times[c]}.')
        sleep(0.5)
  print('-'*20)
  sleep(0.3)
  if opcao == '2':
    print('Os 4 últimos times são:')
    for pos, c in enumerate(times[16:]):
      pos = pos + 17
      print(f'{pos}º{c}.')
      sleep(0.2)
  print('+'*20)
  if opcao == '3':
      print('Times em ordem alfabética: ')
      for c in sorted(times):
          print(f'{times.index(c)+1}º{c}.')
          sleep(0.5)
  print('+'*20)
  if opcao == '4':
    clube=input('Digite o nome do seu time: ')
    if clube in times:
          print(f'O {clube} está na posição {times.index(clube)+1}°')
    else:
      print('Seu time não está na lista.')
      sleep(0.3)
  sair = ' '
  while sair not in 'SN':
    sair=input('Deseja continuar?[s/n]: ').upper().strip()[0]
  if sair == 'N':
    break
print('Encerrando...')
sleep(1)
print('Obrigado e fique ligado nas novidades do Brasileirão.')

    





        



