#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
# fazer um laço dentro do outro para preencher as linhas e colunas:
for linha in range(0,3):
    for coluna in range(0,3):                       ## laço para coluna
        matriz[linha][coluna]= int(input(f'Digite um valor para [{linha}, {coluna}]: '))    # botar as coordenadas da matriz para linhas e colunas
print('+'*30)
# 2 parte : MOSTRAR A ESTRUTURA NA TELA: Outro duplo laço de repetição
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')    # Formatar os espaços CENTRALIZADO PARA NÚMEROS COM CASAS DECIMAIS MAIORES: ':^5'
    print()     # Formatar para matrix, quebra a linha com o print,      


        
