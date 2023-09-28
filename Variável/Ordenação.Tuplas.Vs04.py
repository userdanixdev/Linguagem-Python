from time import sleep
times = 'Internacional', 'São Paulo', 'Flamengo', 'Atlético-MG', 'Palmeiras',\
        'Grêmio', 'Fluminense', 'Ceará', 'Corinthians', 'Santos', 'Atletico-PR',\
        'Atletico-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia', 'Goiás',\
        'Coritiba', 'Botafogo'
print(f'{"="*50}\n{"Tabela do Brasileirão":^48}{"="}\n{"="*50}')
sleep(1)
print('A tabela completa: ')
for c in range (0,20):
    sleep(0.3)
    print(f'{c+1}°{times[c]}')
print("="*50)
while True:
    opção = ' '
    while opção not in '1234':
        opção = str(input('''
[1] - 5 Primeiros colocados
[2] - 5 Ultimos colocados
[3] - Lista com os times em ordem alfabética
[4] - Posição do time Fluminense 
Escolha uma das opções acima:'''))
    print('--' * 45)
    if opção == '1':
        print(f'O TOP 5 do Campeonato são: \n{times[0:6]} ')
    if opção == '2':
        print(f'Os 5 últimos colocados são, respectivamente: \n{times[-5:]}')
    if opção == '3':
        print(f'Lista em ordem alfabética: \n{sorted(times)}')
    if opção == '4':
        print(f'O Fluminense se encontra na {len(times[0:7])}° posição')
    print('--' * 45)
    sleep(1)
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if sair == 'N':
        break
print('Encerrando...')
sleep(1.2)
print('Obrigado! Cadastre-se e fique ligado nas novidades do Brasileirão!!')

Obs: ** Ordenação do conteúdo da tupla na versão 4 diferente da versão 05 **





























