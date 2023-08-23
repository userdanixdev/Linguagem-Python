#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range (1,6):
    peso=float(input(f'Peso da {p}ª pessoa: '))
    if p ==1:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior = peso
        if peso<menor:
            menor = peso
print(f'''
        O maior peso lido foi de {maior} KG.
        O menor peso lido foi de {menor}KG.  
        ''')            
Result:

Peso da 1ª pessoa: 80
Peso da 2ª pessoa: 65.5
Peso da 3ª pessoa: 45.9
Peso da 4ª pessoa: 55
Peso da 5ª pessoa: 110.5

        O maior peso lido foi de 110.5 KG.
        O menor peso lido foi de 45.9KG.  
=============================================================
            EXEMPLO 02:

#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
lista=[]  #lista vazia
for c in range(1,6):
    peso=float(input(f'Peso da {c}ªpessoa: '))
    lista = lista +[peso] #adc valor da variável peso na lista
print(f'O maior peso foi:',max(lista)) # função max adc
print(f'O menor peso foi:',min(lista)) # função min adc')

Results:
Peso da 1ªpessoa: 110
Peso da 2ªpessoa: 112
Peso da 3ªpessoa: 115
Peso da 4ªpessoa: 120
Peso da 5ªpessoa: 100
O maior peso foi: 120.0
O menor peso foi: 100.0
======================================================================

#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

pesos=[float(input(f'Peso da {x}ªpessoa: '))for x in range(1,6)]
print(f'O maior peso foi de {max(pesos)}KG.')
print(f'O menor foi de {min(pesos)}KG.')

Result:
Peso da 1ªpessoa: 50
Peso da 2ªpessoa: 51
Peso da 3ªpessoa: 45
Peso da 4ªpessoa: 100
Peso da 5ªpessoa: 99
O maior peso foi de 100.0KG.
O menor foi de 45.0KG.
=======================================================================

            
