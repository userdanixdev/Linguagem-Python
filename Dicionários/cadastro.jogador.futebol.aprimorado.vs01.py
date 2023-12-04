
#Cadastro.Jogador.Futebol.Aprimorado

#Aprimore o programa de 'cadastro de jogador de futebol'
#93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento
#de cada jogador.

# Conceito: Lista de jogadores em um dicionário e depois dentro do dicionario tem uma lista #

#Versão 01:

galera=[]
jogador={}
gols=[]
while True:
    jogador.clear()
    gols.clear()
    print('='*50)
    jogador['nome']=input('Nome do jogador: ').strip().title()
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1,partidas+1):
        gols.append(int(input(f'-Quantos gols na {p}º partida? ')))
    jogador['gols']=gols.copy()
    jogador['total']=sum(gols)
    galera.append(jogador.copy())
    resp=str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp not in 'SN':
        while resp not in 'SN':
            print('ERRO!.Digite apenas S ou N.')
            resp=str(input('QUer continuar mesmo?[S/N]')).strip().upper()[0]
    if resp in 'S':
        continue
    if resp in 'N':
        break
print('+'*50)
print('Cód-ID Nome     Gols      Total')
for p, v in enumerate(galera):
    print(f'{p:>3}{v["nome"]:<14}{str(v["gols"]):<14}{str(v["total"]):<6}')
while True:
    cod=int(input('Mostrar dados de qual jogador? '))
    if cod<=len(galera):
        print(f'>>> Levantamento do jogador {galera[cod]["nome"]}<<')
        for k,v in enumerate(galera[cod]["gols"]):
            print(f' No jogo {k+1}fez {v} gol(s).')
    opcao=str(input('Quer mostrar dados novamente?[S/N] ')).strip().upper()[0]
    if opcao not in 'SN':
        while opcao not in 'SN':
            print('ERRO. Digite apenas S ou N.')
            opcao=str(input('Quer mostrar os dados?[s/n]')).strip().upper()[0]
    if opcao in 'S':
        continue
    if opcao in 'N':
        break
print('+'*60)
print('Encerrando programa.')






