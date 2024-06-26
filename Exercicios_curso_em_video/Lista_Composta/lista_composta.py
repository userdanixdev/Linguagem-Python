# Lista composta:

lista_temporaria = []
lista_principal = []
maior_peso = 0
menor_peso = 0

while True:
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Peso: ')))
    if len(lista_principal) == 0:
        maior_peso = menor_peso = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior_peso:
            maior_peso = lista_temporaria[1]
        if lista_temporaria[1] < menor_peso:
            menor_peso = lista_temporaria[1]
    # Gera uma cópia da lista temporaria na lista principal
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()  # A lista temporaria está salva dentro da principal
    resposta = input('Quer continuar? [S/N] ')
    if resposta in 'Nn':
        break
print(f'Os dados foram:{lista_principal}.')
print(f'Ao todo você cadastrou {len(lista_principal)} pessoas.')
print(f'O maior peso foi de {maior_peso}KG.')
print(f'O menor peso foi de {menor_peso}KG.')
print('O maior peso foi de: ',end='')
for p in lista_principal:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {menor_peso}KG. Peso de ',end='')
for p in lista_principal:
    if p[1] == menor_peso:
        print(f'[{p[0]}].',end='')
print()        


