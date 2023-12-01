#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

#VERSÃO 03:

entrada_1=str(input('Nome: '))
entrada_2=float(input('Média: '))
print('+'*30)
if entrada_2 <= 5:
    entrada_3 = 'Reprovado'
elif entrada_2 <= 6.9:
    entrada_3 = 'Recuperação'
else:
    entrada_3 = 'Aprovado'
ficha={'nome':entrada_1, 'média':entrada_2,'status':entrada_3}
print(f'Nome do aluno:{ficha["nome"]}')
print(f'Média do aluno:{ficha["média"]}')
print(f'Status:{ficha["status"]}')

