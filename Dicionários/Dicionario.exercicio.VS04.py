#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

#VERSÃO 04:

print()
while True:
    aluno={'Nome':str(input('Nome do aluno: ')).strip().title(),'Média':float(input(f'Média:'))}
    while aluno['Média']<0 or aluno['Média']>10:
        aluno['Média']=float(input('Média Inválida, tente novamente:'))
    if aluno['Média']>=6:
        aluno['Situação']='Aprovado'
    elif 5 <= aluno['Média']<6:
        aluno['Situação']='Em recuperação'
    else:
        aluno['Situação']='Reprovado'
    print('+'*30)
    for key, value in aluno.items():
        print(f'{key}:{value}')
    print('+'*30)
    print()

    continuar=str(input('Deseja verificar a situação de outro aluno?[S/N]')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Opção Inválida, tente novamente: ')).strip().upper()
    if continuar == 'N':
        break
print('Programa finalizado')    
