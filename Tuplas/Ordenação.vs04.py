from time import sleep
times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

print(f'{"="*50}\n{"Tabela do Brasileirão 2023":^48}\n{"="*50}')
sleep(1)
print('A tabela completa: ')
for c in range(0,20):
    sleep(0.3)
    print(f'{c+1}º{times[c]}')
print('='*15)
while True:
  opcao=' '
  while opcao not in '1234':
    opcao = (input('''
[1] - 5 Primeiros colocados
[2] - 5 Ultimos colocados
[3] - Lista com os times em ordem alfabética
[4] - Posição do time Fluminense 
Escolha uma das opções acima:'''))
    print('='*40)
    if opcao == '1':
      print(f'O 5 primeiros colocados no Brasileirão são: \n{times[0:6]} ')
    if opcao == '2':
      print(f'Os 5 últimos colocados são, respectivamente:\n{time[-5]}')
    if opcao == '3':
      print(f'Lista em ordem alfabética: \n{sorted(times)}')
    if opcao == '4':
      while True:
        clube=input('Digite o nome do seu time: ').capitalize()
        if clube in times:
          print(f'O {clube} está na posição {time.index(clube)+1}º.')
          break
        else:
          print('Seu time não está na lista.')
          sleep(1)
sair = ' '
while sair not in 'SN':
      sair = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
if sair == 'N':
    break
print('Encerrando...')
sleep(1)
print('Obrigado. Cadastre-se e fique ligado nas novidades do Brasileirão.')
    
