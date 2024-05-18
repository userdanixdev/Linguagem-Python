# Unindo dicionários e listas:

# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa=dict()
galera=list()
soma= média = 0   # Preciso então de um contador iniciando do 0  ##B
while True:
    pessoa.clear()   # limpa os dados 'pessoa' para garantir que os dados da pessoa anterior não afetem a próxima iteração
    pessoa['Nome']=input('Nome: ')
    while True:     # Validação para somente 'Mm' ou Ff'
        pessoa['Sexo']=input('Sexo: [M/F] ').upper()[0]  # .upper pra jogar pra maiúsculo e [0] pra pegar a primeira letra.
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade']=int(input('Idade: '))
    soma += pessoa['Idade']  ## Receber a contagem do item B
    galera.append(pessoa.copy())   # Adiciona uma cópia do dicionário 'pessoa' a lista 'galera'
    while True: # Looping infinito sempre que verdade para uma variável de controle de saida
        resp=input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':  # Verifica se a entrada é 'S' ou 'N':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':   # Sai do looping principal:
        break
print('+'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')  # A
# Para ter a média das idades eu tenho que ter a soma das idades.   #B
média= soma/len(galera)  # Esse é o cálculo da média
print(f'A média de idade é de {média:5.2f} anos.')
##C = Lista com todas as mulheres:
#print('As mulheres cadastradas foram: ', end='')  RETIREI ESSE PRINT E COLOQUEI DENTRO DO LAÇO
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'As mulheres cadastradas foram:{p["Nome"]} ',end='')
print()
#D:
print(f' Lista das pessoas que estão acima da média: ', end='')
for p in galera:   # Percorre a lista gelera e verifica se a idade da pessoa é maior ou igual à média.
    if p['Idade']>=média:
        print('    ', end='')
        for k, v in p.items():  # Dentro do looping, usamos a variável de execução 'p' com a função 'items' para percorrer a lista galera e
                                # verifica se a idade da pessoa, se for, imprime 'chave=valor'
            print(f'{k} = {v}; ',end='')
        print()
print('+++ ENCERRADO +++')        



        
      


