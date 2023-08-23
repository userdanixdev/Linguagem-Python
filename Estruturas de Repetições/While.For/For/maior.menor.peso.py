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
            
