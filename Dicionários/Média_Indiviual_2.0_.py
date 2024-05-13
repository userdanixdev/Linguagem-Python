#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

#VERSÃO 02:

# Obs : A sintaxe para {chave:valor} sem fechar o parênteses irá fazer com que outros declarações de dicionario seja escritas por cima.
# Ao listar um dicionário, a função items poderá percorrer as listas criadas dentro do dicionário
# No entanto, não há necessidade de criar uma lista vazia
aluno={'Nome':str(input('Nome: '))} # Variável aluno recebe chave nomeada 'nome' e entrada do usuário dentro do dicionário
aluno['Média']=float(input(f'Digite a média de {aluno["Nome"]}: '))
aluno['Situação']='aprovado'if aluno['Média']>=7 else 'Reprovado' if aluno['Média']<6 else 'Recuperação'
for key,value in aluno.items(): # Percorrer chaves e valores do dicionário
    print(f'{key}:',value)
