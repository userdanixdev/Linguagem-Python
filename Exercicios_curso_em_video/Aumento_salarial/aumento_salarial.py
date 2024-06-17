# Aumento Salarial :

while True:
    nome=(input('Qual o nome do empregado: '))
    salario = float(input('Qual o salário atual? '))
    aumento=float(input('Quantos por cento? '))
    novo_salario = salario*((100+aumento)/100)
    print(f'O funcionário {nome} que ganhava R$ {salario:.2f} com {aumento:.0f}%',end=''
          f' de aumento, passa a receber R${novo_salario:.2f}.\n')
    continuar = input('Deseja continuar? [1-SIM & 2-NÃO]')
    if continuar == '1':
        continue
    if continuar == '2':
        break
print('fim')    
    

