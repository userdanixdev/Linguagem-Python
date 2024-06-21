# Extraindo vogais de uma tupla:
# Versão 04:

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

contagem = 0
vogais_find = ''
for c in range(0,len(palavras)):
    for d in range(0,len(palavras[c])):
        if palavras[c][d] in vogais[:]:
            contagem += 1
            vogais_find += palavras[c][d]
    print(f'Na palavra: {palavras[c]} tem {contagem} vogais. São elas: {vogais_find}')
    contagem = 0      # Se não vai somar cada vogais e o resultado será diferente.
    vogais_find = ''  # Se não vai contar as vogais das outras palavras. 
    
            
    
    
