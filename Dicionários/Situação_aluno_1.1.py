# crie um programa que leia o nome e média de um aluno, guardando
# também a situação em um dicionário,
# No final mostre o conteúdo da estrutura na tela.

# Versão 1.1:
from time import sleep

print(f'{'+'*30}\n{"Situação do aluno":^28}\n{'+'*30}\nInsira os dados abaixo:')
sleep(0.7)
aluno = dict() # Nomear uma variável como dicionário ou por {}
aluno['nome'] = str(input('Nome: ')) # Chave aluno recebe entrada ao usuário
aluno['média']= float(input(f' Média de {aluno["nome"]}: ')) # Chave média deve receber entrada do usuário
# Condições de saída:
if aluno['média']>=7:
    aluno['situação']='Aprovado' # Se a média for maior ou igual a 7 o aluno recebe uma chave situação com valor 'aprovado'
elif 5 <= aluno['média']<7:
    aluno['situação']='Recuperação' # Se a média for menor ou igual a 5 e menor que 7
else:
    aluno['situação']='Reprovado' # Se não satisfazer as condiçõs if e elif a chave situação recebe 'reprovado'.
sleep(0.7)
print(f' Dados do dicionário aluno:\n {aluno}')
sleep(0.7)
print('*'*10 + 'Percorrendo o dicionário' + '*'*10)
# percorrendo o dicionário:
for k, v in aluno.items():
    print(f' Chave:{k} é igual a valor:{v}.')
    sleep(0.7)
print('Fim')
