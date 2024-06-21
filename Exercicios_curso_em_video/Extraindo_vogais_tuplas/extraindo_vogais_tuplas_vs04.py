print()

contagem = 0
vogais_find = ''
for c in range(0,len(palavras)):
    for d in range(0,len(palavras[c])):
        if palavras[c][d] in vogais[:]:
            contagem += 1
            vogais_find += palavras[c][d]
    print(f'Na palavra: {palavras[c]} tem {contagem} vogais. São elas: {vogais_find}')
    contagem = 0
    vogais_find = ''
    
            
    
    
