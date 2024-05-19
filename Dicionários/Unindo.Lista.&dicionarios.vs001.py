#Unindo dicionários e listas

#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários
#em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

#VERSÃO 001:

#pessoa=dict()    # o .clear não precisa para dicionários, os valores vão sendo substituidos.

dic={}       # Inicializa um dicionário vazia para armazenar dados temporários de cada pessoa
pessoas = [] # Inicializa uma lista vazia para armazarnar todos os dicionários de pessoas
media = 0    # Inicializa a variável media para somar as idades das pessoas
while True:
    dic['Nome']=input('Nome: ').strip().title()  # Cria uma chave 'Nome' para o usuário inserir o valor. strip() para remover os espaços e capitalizar a string com title()
    dic['Idade']=int(input('Idade: '))           # Cria uma chave chamada 'idade' para o usuário inserir a idade em número inteiro
    dic['Sexo']=input('Sexo: [M/F]').strip().upper()[0] # Cria-se a chave 'sexo' para o usuário inserir o valor. Uso da função 'strip' e 'upper' para remover espaços e converter para maiúscula e pega o primeiro caractere
    while dic['Sexo']!='M' and dic['Sexo']!='F': # Validação da entrada do sexo
          dic['Sexo']=input('Decisão inválida. Sexo somente [M/F]: ').upper()[0] 
    pessoas.append(dic.copy())                   # Cópia do dicionário para lista 'pessoas'
    decision=input('Deseja continuar o cadastro? [S/N]').upper()[0] # Variável de entrada de decisão
    while decision != 'S' and decision != 'N':   # Validação da decisão
        decision=input('Decisão inválida. Deseja continuar?[S/N]').upper()[0]
    if decision in 'Nn':
        break
    for v in range(0,len(pessoas)): # Calcula a soma das idades para obter a média
        media = media + pessoas[v]["Idade"]
# Resultados na tela:
print(f' A) O total de pessoas cadastradas foram {len(pessoas)}.')
print(f' B) A média das idades foram {media/len(pessoas):.2f}.')    
print(f' C) As mulheres cadastradas foram: ',end=' ')
for v in range(0,len(pessoas)): # Looping que percorre o comprimento da lista pessoas de 0 ao comprimento.
    if pessoas[v]["Sexo"]=='F': # O 'v' - Acessa o dicionário da pessoa na posição 'v' da lista 'pessoas'/ # Acessa o valor associado à chave 'Sexo' no dicionário pessoa.
        print(f'{pessoas[v]["Nome"]}', end=' ') # String formatada que inclui valor associado a chave 'nome'.
print()
print(' A lista de pessoas com idade acima da média: ')
for v in range(0,len(pessoas)): # Variável de execução 'v' percorre em looping no intervalo de 0 ao tamanho da lista pessoas 
    if pessoas[v]["Idade"] >= media/len(pessoas): # Condicional em que o valor 'v' associado a chave 'idade'  for mais que a média
        print(f'Nome: {pessoas[v]["Nome"]},Idade:{pessoas[v]["Idade"]}, Sexo: {pessoas[v]["Sexo"]}')
        # Strings formatadas que inclue na ordem valor e chave.
print()


        
    

        
      


