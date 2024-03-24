# Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# A - A soma de todos os valores pares digitados
# B - A soma dos valores da terceira coluna
# C - O maior valor da segunda linha

matriz=[[],[],[]]
# 1° PASSO:
    # Declarar variáveis para incrementar os desafios propostos:
soma_par = maior_valor = soma_coluna = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite o número nas posições x e y:{linha,coluna}: ')))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
        if matriz[linha][coluna] % 2 == 0:   # SOMA DOS VALORES PARES
            soma_par += matriz[linha][coluna]
    print()
print('='*30)
print(f'A soma dos valores pares é: {soma_par}.')
# Soma dos valores da TERCEIRA COLUNA:
for linha in range(0,3):
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {soma_coluna}.')
# MAIOR VALOR DA SEGUNDA LINHA:
for coluna in range(0,3):
    if coluna == 0:
        maior_valor = matriz[1][coluna]
    elif matriz[1][coluna]>maior_valor:
        maior_valor = matriz[1][c]
print(f'O maior valor da segunda linha é:{maior_valor}.')        
        
