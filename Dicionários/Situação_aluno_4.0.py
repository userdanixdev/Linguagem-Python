#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

# Versão 04:
while True : # Usando looping infinito sempre que verdade
    aluno={'Nome':str(input('Nome do aluno: ')).strip().title(),'Média':float(input(f'Média: '))}
    # Variável recebe um dicionário comprimido com duas chaves e duas entradas para o usuário para tipos de dados diferentes
    # O método strip() remove os espaços e o método title() usado para strings para transformar em maiúscula a primeira letra
    while aluno['Média']<0 or aluno['Média']>10: # Looping infinito com condições
        aluno['Média']=float(input('Média inválida, tente novamente: '))
    if aluno['Média']>=6:
        aluno['Situação']='Aprovado' # Por essa condição o dicionário ganha uma nova chave com um novo valor
    elif 5 <= aluno['Média']<6:
        aluno['Situação']= 'Recuperação'
    else:
        aluno['Situação']= 'REPROVADO' # Não satisfazendo as condições a chave nomeada recebe outro valor.
    print('+'*30)
    # Percorrendo o dicionário aluno
    for key,value in aluno.items():
        print(f'{key}:{value}')
    print('='*15)
    print()
    # Variável de controle para repetir a operação ou finalizar
    continuar=str(input('Deseja verificar a situação de outro aluno?[S/N]')).strip().upper()
    # Condicionar a saída: somente 's' e 'n' senão for, repete o looping:
    while continuar not in 'SN': 
        continuar = str(input('Opção inválida. Tente novamente: ')).strip().upper()
    if continuar == 'N':
        break
print('Programa finalizado')    
    


        
