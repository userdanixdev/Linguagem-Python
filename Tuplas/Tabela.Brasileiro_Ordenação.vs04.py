import sys
times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

print(f'{"="*50}\n{"Tabela do Brasileirão 2023":^48}\n{"="*50}')
sleep(1)
print('A tabela completa: ')
# Criar um intervalo de 1 a 20 para listar e mostrar a tabela do Brasileirão lembrando que em
# Python a contagem começa com 0, então acrescentar 1
for c in range(0,20):
    sleep(0.3)
    print(f'{c+1}º{times[c]}')
print('='*15)
while True:
    opcao=' '
    sleep(1)
    while opcao not in '1234':
        opcao = (input('''
Escolha uma das opções abaixo:
[1] - 5 Primeiros colocados
[2] - 5 Ultimos colocados
[3] - Lista com os times em ordem alfabética
[4] - Posição do time
[5] - Sair
'''))
        print('='*40)
        if opcao == '1':
            print(f'Os 5 primeiros colocados no Brasileirão são: \n{times[0:6]}')
        if opcao == '2':
            print(f'Os 5 últimos colocados são, respectivamente: \n{times[-5:]}')
        if opcao == '3':
            for t in sorted(times):
                print(f'{t}')
                sleep(0.3)
            #print(f'Lista em ordem alfabética:\n{"\n".join([f"{t}" for t in sorted(times)])}')
                # Usamos o .join para juntar os elementos da lista separada por espaço.
            print('+'*41)
        if opcao == '4':
            while True:
                clube = input('Digite o nome do seu time: ').capitalize()
                if clube in times:
                    print(f'O {clube} está na posição {times.index(clube)+1}º')
                    break
                else:
                    print('Seu time não está na lista.')
                    sleep(1)
        if opcao == '5':
            sair =' '
            while sair not in 'SN':
                  sair = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
            if sair == 'N':
                sys.exit('Obrigado por usar o programa. Até mais.')
            elif sair == 'S':
                break # volta ao início do llop do menu opções
