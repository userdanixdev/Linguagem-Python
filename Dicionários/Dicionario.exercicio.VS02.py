#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

#VERSÃO 02:

aluno={'nome':str(input('Nome: '))}
aluno['média']=float(input(f'Digite a média de {aluno["nome"]}: '))
aluno['Situação']='aprovado' if aluno['média']>=7 else 'Reprovado' if aluno['média']<6 else 'Recuperação'
for key,value in aluno.items():
    print(f'{key}:', value)


