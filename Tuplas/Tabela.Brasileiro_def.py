# Versão Modelagem Funcional :
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

from time import sleep
import sys

def exibir_tabela_completa(times):
    '''Função para exibir a tabela completa'''
    print(f'{"="*50}\n{"Tabela do Brasileirão 2023":^48}\n{"="*50}')
    sleep(1)
    print('A tabela completa: ')
    for c in range(20):
        sleep(0.3)
        print(f'{c+1}° {times[c]}')
    print('='*15)

def exibir_primeiros_colocados(times):
    '''Função que exibe os primeiros colocados'''
    print('Os primeiros colocados são: ')
    for i in range(5):
        print(f'{i+1}° {times[i]}')

def exibir_ultimos_colocados(times):
    '''Função que exibe os 5 últimos colocados'''
    print('Os últimos 5 colocados são, respectivamente: ')
    for i in range(-5,0):
        print(f'{len(times)+i+1}° {times[i]}')

def exibir_times_ordem_alfabetica(times):
    '''Função que exibe a lista em ordem alfabética'''
    for t in sorted(times):
        print(t)
        sleep(0.3)
    print('='*41)

def exibir_posicao_time(times):
    '''Função para exibir a posição de um time específico'''
    while True:
        clube=input('Digite o nome do seu time: ').capitalize()
        if clube in times:
            print(f'O {clube} está na posição {times.index(clube)+1}°')
            break
        else:
            print('Seu time não está na lista.')
            sleep(1)

def sair_programa():
    '''Pergunta ao usuário se ele deseja sair do programa'''            
    while True:
        sair = input('Deseja continuar? [S/N]: ').upper().strip()
        if sair == 'N':
            sys.exit('Obrigado por usar o programa. Até mais.')
        elif sair == 'S':
            return
        else:
            print("Opção inválida. Escolha S para continuar ou 'N' para sair.")
def main():
    times = (
        'Botafogo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Fluminense',
        'Atlético-PR', 'São Paulo', 'Fortaleza', 'Cruzeiro', 'Bragantino', 'Santos',
        'Internacional', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco',
        'Coritiba'        )
    exibir_tabela_completa(times)        
    while True:
        opcao = input('''
                      Escolha uma das opções abaixo:
                        [1] - 5 Primeiros colocados
                        [2] - 5 Últimos colocados
                        [3] - Lista com os times em ordem alfabética
                        [4] - Posição do time
                        [5] - Sair
''')
        print('='*40)
        if opcao =='1':
            exibir_primeiros_colocados(times)
        elif opcao == '2':
            exibir_ultimos_colocados(times)
        elif opcao == '3':
            exibir_times_ordem_alfabetica(times)
        elif opcao == '4':
            exibir_posicao_time(times)
        elif opcao == '5':
            sair_programa()

main()
