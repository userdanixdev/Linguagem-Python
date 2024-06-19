# Analise de dados:
# Versão 02:

m = 0
f = 0
maiores = 0
while True:
    print('Cadastro')
    idade = int(input('Digite sua idade: '))
    while idade < 1 or idade > 150:
        print('Digite uma idade entre 1 a 150.')
        idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        maiores += 1
    sexo=input('Qual é o seu sexo? ').strip().upper()[0]
    while sexo not in 'MF':
        print('Digite a opção correta.')
        sexo=input('Qual o seu sexo? [M/F]: ').strip.upper()[0]
    if sexo == 'M':
        m += 1
    elif sexo == 'F' and idade < 20:
        f += 1
    print()
    continuar = input('Deseja continuar [S/N] ?').strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida.')
        continuar = input('Deseja continuar? ').strip().upper()[0]
    if continuar == 'N':
              break
print(f'{maiores} pessoas são maiores de 18 anos\n{f} são mulheres com menos de 20 anos\n{m} são homens.')            
