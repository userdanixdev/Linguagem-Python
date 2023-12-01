#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

aluno = dict() ## ou chaves {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] =  float(input(f'Média de {aluno["nome"]}: '))
if aluno['média']>=7:
    aluno['situação']= 'Aprovado'
elif 5 <= aluno['média']< 7:
    aluno['situação']= 'Recuperação'
else:
    aluno['situação']= 'Reprovado'
print(aluno)
# Com o print o resultado no console para o usuário ver sai:
#Nome: Daniel
#Média deDaniel: 6.5
#{'nome': 'Daniel', 'média': 6.5, 'situação': 'Recuperação'}
# Sendo assim, mais formatado:
for k, v in aluno.items():   # 'k' para keys, 'v' para values
    print(f'{k} é igual a {v}. ')



