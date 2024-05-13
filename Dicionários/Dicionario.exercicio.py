#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

aluno = dict() ## ou chaves {}
aluno['nome'] = str(input('Nome: ')) # Chave aluno recebe entrada ao usuário
aluno['média'] =  float(input(f'Média de {aluno["nome"]}: ')) # Chave média deve receber entrada do usuário
# Condições de saída:
if aluno['média']>=7:
    aluno['situação']= 'Aprovado' # Se a média for maior ou igual a 7 o aluno recebe uma chave situação com valor 'aprovado'
elif 5 <= aluno['média']< 7:
    aluno['situação']= 'Recuperação' # Se a média for maior ou igual a 7 o aluno recebe uma chave situação com valor 'aprovado'
else:
    aluno['situação']= 'Reprovado' # Se não satisfazer as condiçõs if e elif a chave situação recebe 'reprovado'.
print(aluno)
# Com o print o resultado no console para o usuário ver sai:
#Nome: Daniel
#Média deDaniel: 6.5
#{'nome': 'Daniel', 'média': 6.5, 'situação': 'Recuperação'}
# Sendo assim, mais formatado:
for k, v in aluno.items():   # 'k' para keys, 'v' para values, a função items() irá percorrer todos os dicionários de aluno em função do looping 'for':
    print(f'{k} é igual a {v}. ')



