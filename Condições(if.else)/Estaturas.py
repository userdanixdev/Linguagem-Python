#Criar um programa que mostre a estatura de três pessoas diferentes.
#Se existir estatura igual exibir uma mensagem de semelhança.
# Caso contrário, o programa deve informar a maior estatura.

estatura01=float(input('Digite a estatura número 1: '))
estatura02=float(input('Digite a estatura número 2: '))
estatura03=float(input('Digite a estatura número 3: '))

if estatura01 == estatura02 or estatura01==estatura03 or estatura02==estatura03:
    print('Há pelo menos, 2 pessoas com a mesma estatura.')
elif estatura01>estatura02 and estatura01>estatura03:
    print(f'A pessoa mais alta tem {estatura01}m')
elif estatura02>estatura01 and estatura02>estatura03:
    print(f'A pessoas mais alta tem {estatura02}m ')
else:
    print(f'A pessoas mais alta tem {estatura03}m.')
                 
Result:

Digite a estatura número 1: 1.89
Digite a estatura número 2: 1.77
Digite a estatura número 3: 1.69
A pessoa mais alta tem 1.89m
===================================================================================================
