# Versão 03:

import random
n = (random.randint(0,10),random.randint(0,10),
     random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(f'Os números sortados foram: {n}.')
cont = 0
maior = 0
menor = 5
while True:
    for r in range(0,5):
     if maior <= n[r]:
        maior = n[r]
     if menor >= n[r]:
            menor = n[r]
    cont += 1
    if cont  == 5:
        break
print(f'O maior é {maior} e o menor é {menor}.')    




