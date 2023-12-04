
#Cadastro.Jogador.Futebol.Aprimorado

#Aprimore o programa de 'cadastro de jogador de futebol'
#93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento
#de cada jogador.

# Conceito: Lista de jogadores em um dicionário e depois dentro do dicionario tem uma lista #

time=list() # 1°Passo para a aprimoração
jogador=dict()
partidas=list()
#Leitura dos dados dos jogadores:
while True:
    jogador.clear()
    jogador['Nome']=str(input('Nome do jogador: '))
    tot= int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Gols']=partidas[:]   # Irá receber cópias de partidas.
    jogador['Total de gols:']=sum(partidas)
    time.append(jogador.copy())
# Para aprimorar o código com cadastros de mais jogadores:
    while True:
        resp=(input('Quer continar?[S/N] ')).upper()[0]  # 2°Passo para aprimoração
        if resp in 'SN':
            break
        print('ERRO. Responda apenas S ou N.')
    if resp == 'N':
        break
# Cabeçalho da tabela:
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()    
print('+'*30)
#Criação da tabela de jogadores:
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('+'*30)
# Operação para BUSCAR dentro do dicionário os dados do jogador:
while True:
    busca=int(input('Mostrar dados de qual jogador? 999 para parar. '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO. Não existe jogador com código {busca}.')
    else:
        print(f' --> Levantamento do jogador {time[busca]["Nome"]}.')
# MOstrar o levantamento:
        for indice, gols in enumerate (time[busca]["Gols"]):
            print(f' ---> No jogo {indice+1} fez {gols} gols.')
    print('+'*40)
print('VOlte sempre')    








