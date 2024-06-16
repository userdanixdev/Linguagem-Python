# Tabuada :
while True:
    n1 = int(input('Digite um número para ver a sua tabuada: '))
    for n2 in range(1,11):
        resultado=n1*n2
        print(f'{n1} X {n2} = {resultado}')
    continuar = input('Quer continuar? [S/N]')
    if continuar.capitalize() == 'N':
        break
print('Fim')
    
