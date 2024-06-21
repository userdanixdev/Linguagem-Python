class CampeonatoBrasileiro:
    def __init__(self):
        
        self.times=('Palmeiras','Atlético-MG','Flamengo','Grêmio','Botafogo',
       'RB Bragantino','Fluminense','Athletico','São Paulo',
       'Cuiabá','Corinthians','Cruzeiro','Santos','Vasco','Bahia','Goiás',
       'Coritiba','América-MG','Atlético-GO','Fortaleza')

    def programa_1(self):

        from time import sleep
        print('Tabela do Campeonato Brasileiro 2023')
        sleep(2)
        print(f'Lista de times:{self.times}.')
        sleep(2)
        print(f'\nLista formatada: \n')
        for t in self.times:
            sleep(0.2)
            print(t)
        sleep(2)            
        print(f'\nOs 5 primeiros são:\n {self.times[0:5]}.')
        sleep(2)
        print(f'\nOs 4 últimos são:\n {self.times[-4:]}.')
        sleep(2)
        print(f'\nOs times em ordem alfabética:\n{sorted(self.times)}.')
        sleep(2)
        print(f'\nO Fortaleza está na {self.times.index("Fortaleza")+1}º posição.')

    def programa_2(self):

        from time import sleep
        sleep(2)
        print(f'{"+"*40}\nCampeonato Brasileiro 2023:\n{"+"*40}\n{self.times}.')
        sleep(0.5)
        print(f'Os 5 primeiros colocados foram:\n{self.times[0:5]}\n')
        sleep(2)
        print(f'Os clubes classificados para a Libertadores:\n{self.times[0:6]}\n')
        sleep(2)
        print(f'Os clubes que vão para a pré-libertadores:\n{self.times[6:8]}\n')
        sleep(2)
        print(f'Os clubes que classificados para a sul-americana:\n{self.times[8:14]}\n')
        sleep(2)
        print(f'Os clubes rebaixados foram:\n{self.times[16:]}\n')
        sleep(2)
        print(f'Os times em ordem alfabética:\n{sorted(self.times)}\n')
        sleep(2)
        print(f'O Fortaleza está na {self.times.index("Fortaleza")+1}º posição.')
        sleep(2)
        
    def iniciar(self):
        from time import sleep
        
        print('Programa 1')
        self.programa_1()
        sleep(3)
        print('Programa 2')
        self.programa_2()
        sleep(2)
        print('Programa 3 - Uso do "for in range"')
        self.programa_3()
        sleep(2)
        print('Programa 4- Uso do enumerate e menu de opções')
        self.programa_4()

    def menu_programas(self):
        while True:
            try:
                opcao=int(input('''
            Escolha qual programa quer visualizar:
            
            [1] - Programa 1 - Tab. Camp Brasileiro(Sem formatação)
            [2] - Programa 2 - Tab. Camp Brasileiro(Sem format c/ informações adicionais)
            [3] - Programa 3 - Tab. Camp Brasileiro(Uso de laco for e range)
            [4] - Programa 4 - Tab. Camp Brasileiro(Menu de opções e uso do enumerate)
            [5] - Rodar todos os programas 
            [0] - Sair dos programas
            
            Escolha: '''))
            except ValueError:
                print('Entrada inválida. Por favor, digite somente os números de 0 a 5.')
                continue
            if opcao in range(6):
                if opcao == 1:
                    self.programa_1()
                elif opcao == 2:
                    self.programa_2()
                elif opcao == 3:
                    self.programa_3()
                elif opcao == 4:
                    self.programa_4()
                elif opcao == 5:
                    self.iniciar()
                elif opcao == 0:
                    print('Saindo do programa...')
                    break
            else:
                 print('Opção inválida.Tente novamente.')

    def programa_3(self):

        from time import sleep
        sleep(1)
        print('Campeonato Brasileiro 2023\nTabela Completa:\n')
        for contagem in range(0,len(self.times)):
            sleep(0.2)
            print(f'{contagem+1}º{self.times[contagem]}.')
        print('\nOs 5 primeiros colocados:\n')
        for contagem in range(0,5):
            sleep(0.2)
            print(f'{contagem+1}º{self.times[contagem]}.')
        print('\nOs 4 últimos colocados:\n')
        for contagem in range(16,len(self.times)):
            sleep(0.2)
            print(f'{contagem+1}º{self.times[contagem]}.')
        print('\nTabela em ordem alfabética:\n')
        for contagem in range(0,len(self.times)):
            sleep(0.2)
            print(f'{contagem+1}-{sorted(self.times)[contagem]}.')

    def programa_4(self):

        from time import sleep

        opcao = 0
        while opcao != 8:
            sleep(3)
            try:
                opcao=int(input('''
                   Campeonato Brasileiro 2023:
            [1] -  O campeão do campeonato
            [2] - Classificados para a COMMEBOL Libertadores
            [3] - Classificados para pré-Libertadores
            [4] - Classificados para a Sul-Americana
            [5] - Rebaixados para a série B
            [6] - Posição e situação de um clube
            [7] - Tabela completa
            [8] - Sair do programa
            \nDigite: '''))
            except ValueError:
                print('Entrada inválida. Digite somente os números de 1 a 8.')
                continue
            if opcao == 1:
                print(f'O campeão foi {self.times[0]}.')
            elif opcao == 2:
                print(f'Classificados para a Libertadores 2024:\n')
                for posicao,time in enumerate(self.times[:6]):
                    sleep(0.2)
                    print(f'{posicao+1}º{time}.')
            elif opcao == 3:
                print(f'Clubes que irão participar da Pré-Libertadores 2024:\n')
                for posicao,time in enumerate(self.times[6:8]):
                    sleep(0.3)
                    print(f'{posicao+6}º{time}.')
            elif opcao == 4:
                print(f'Classificados para a Sul-Americana 2024:\n')
                for posicao,time in enumerate(self.times[8:13]):
                    sleep(0.3)
                    print(f'{posicao+8}º{time}.')
            elif opcao == 5:
                print(f'Rebaixados para a Segunda Divisão (Série B):\n')
                for posicao,time in enumerate(self.times[-4:]):
                    sleep(0.3)
                    print(f'{posicao+17}º{time}.')
            elif opcao == 6:
                clube = input('Escreva o nome do seu time: ').strip().title().capitalize()
                if clube in self.times:
                    print(f'O {clube} ficou na {self.times.index(clube)+1}º posição.')
                    print(f'\nSituação: ')
                    if self.times.index(clube) == 0:
                        print('Campeão Brasileiro e vaga garantida na libertadores.')
                    elif self.times.index(clube) >= 1 and self.times.index(clube) <= 5:
                        print('Vaga carimbada na Libertadores.')
                    elif self.times.index(clube) >= 6  and self.times.index(clube) <= 13:
                        print('Vaga na Sul-Americana.')
                    elif self.times.index(clube) >= 16:
                        print('Rebaixado para a série B.')
                    else:
                        print('Ficou na Série A, porém não participa de nenhuma outra competição.')
                else:
                    print(f'O{clube} não participou do Brasileirão 2023.')
            elif opcao == 7:
                cont = 0
                print('Tabela do Brasileirão 2023.')
                for tabela in self.times:
                    sleep(0.3)
                    print(f'{cont+1}º{tabela}.')
                    cont += 1
            print()
                  
                 
                
            
        

if __name__=='__main__':
    campeonato_bra=CampeonatoBrasileiro()
    campeonato_bra.menu_programas()
