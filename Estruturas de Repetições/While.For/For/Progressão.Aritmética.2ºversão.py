#Um professor deseja construir um programa para gerar uma progressão aritmética(PA).
# Para isso devem ser informados 3 argumentos:
#a)primeiro termo:
#b)segundo termo: quantidade de termos
#c)terceiro termo: razão

termo=int(input('Informe o 1ºtermo da P.A: '))
quant_termo=int(input('Informe a quantidade de termos da P.A: '))
razao = int(input('Informe a razão da P.A: '))

print(f'*** {quant_termo} primeiros termos da P.A ***')
print(termo)
for x in range(quant_termo -1):
    termo = termo + razao
    print(termo, end=' ')
    print('*'*38)    

Results:

Informe o 1ºtermo da P.A: 10
Informe a quantidade de termos da P.A: 2
Informe a razão da P.A: 2
*** 2 primeiros termos da P.A ***
10
12 **************************************
=========================================================

