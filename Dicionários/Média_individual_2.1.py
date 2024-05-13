# Crie um programa que leia o nome e média de um aluno, guardando
# também a situação em um dicionário,
# No final mostre o conteúdo da estrutura na tela.

# Versão 2.1:

from time import sleep
print(f'{'+'*30}\n{"Situação do aluno":^30}\n{'+'*30}')
# Obs : A sintaxe para {chave:valor} sem fechar o parênteses irá fazer com que outros declarações de dicionario seja escritas por cima.
# Ao listar um dicionário, a função items poderá percorrer as listas criadas dentro do dicionário
# No entanto, não há necessidade de criar uma lista vazia
aluno={'Nome':str(input('Nome: '))}
aluno['Média']=float(input(f'Digite a média de {aluno["Nome"]}: '))
aluno['Situação']='aprovado' if aluno['Média']>=7 else 'Reprovado' if aluno['Média']<6 else 'Recuperação'
sleep(0.7)
print(f'{'+'*30}\n{"Percorrendo o dicionário ALUNO":^30}\n{'+'*30}')
sleep(0.7)
for key, value in aluno.items():
    print(key,':',value)
    sleep(0.7)
    print('Ou seja...')
    sleep(0.7)
    print('A chave ',key,'contêm o valor: ',value)
print('='*15+' Ou '+'='*15)
for k,v in aluno.items():
    print('A chave ',k,'contêm o valor:',v)
print('FIM')
