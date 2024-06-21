# Tabela do Brasileiro 2023 :
# Versão 02:

from time import sleep

times=('Palmeiras','Atlético-MG','Flamengo','Grêmio','Botafogo',
       'RB Bragantino','Fluminense','Athletico','São Paulo',
       'Cuiabá','Corinthians','Cruzeiro','Santos','Vasco','Bahia','Goiás',
       'Coritiba','América-MG','Atlético-GO','Fortaleza')

opcao = 0
while opcao != 8:
    sleep(3)
    opcao=int(input('''
            Campeonato Brasileiro 2023:
        [1] -  O campeão do campeonato
        [2] - Classificados para a fase de grupos da Libertadores
        [3] - Classificados para pré-Libertadores
        [4] - Classificados para a Sul-Americana
        [5] - Rebaixados para a série B
        [6] - Posição e situação de um clube
        [7] - Tabela completa
        [8] - Sair do programa
        \nDigite: '''))

    if opcao == 1:
        print(f'O campeão foi {times[0]}.')
    elif opcao == 2:
        print(f'Classificados para Libertadores 2024:{times[:6]}.')
    elif opcao == 3:
        print(f'Classificados para a Pré-Libertadores 2024: {times[6:8]}.')
    elif opcao == 4:
        print(f'Classificados para a Sul-Americana 2024: {times[8:14]}.')
    elif opcao == 5:
        print(f'Rebaixados para Segunda Divisão: {times[-4:]}.')
    elif opcao == 6:
        time = input('Escreva o nome do seu time: ').strip().title()
        if time in times:
            print(f'O {time} ficou na {times.index(time)+1}º posição')
            print('Situação: ',end='')
            if times.index(time) == 0:
                print('Campeão Brasileiro e vaga garantida na liberta.')
            elif times.index(time) >= 1 and times.index(time) <= 5:
                print('Vaga na Libertadores.')
            elif times.index(time) >= 6 and times.index(time) < 8:
                print('Pré-Libertadores')
            elif times.index(time) >= 8 and times.index(time) <= 13:
                print('Vaga na Sul-Americana.')
            elif times.index(time) >= 16:
                print('Rebaixado para a série B.')
            else:
                print('Ficou na Série A, porém, não participa de nenhuma outra competição.')
        else:
             print(f'O {time} não participou do Brasileirão 2023.')
    elif opcao == 7:
        cont = 0
        print('Tabela do Brasileirão 2023.')
        for tabela in times:
            print(f'{cont+1}º{tabela}.')
            cont += 1
    print()
print('Fim do programa.')    
            
        



        
              
        
