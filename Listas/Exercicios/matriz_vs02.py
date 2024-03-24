# Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# VERSÃO 02:

matriz=[[],[],[]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite o número nas posições x e y:{linha,coluna}: ')))
for x in matriz:
    print(f'[{x[0]:^5}][{x[1]:^5}][{x[2]:^5}]')
    
        
