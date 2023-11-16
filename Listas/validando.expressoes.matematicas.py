#Crie um programa onde o usuário digite uma expressão qualquer
#que use parênteses.Seu aplicativo deverá analisar se a expressão
#passada está com os parênteses abertos e fechados na ordem correta.

expressao=input('Digite a expressão: ')
pilha=[]   # Lista
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')       # append = adicionar no final da lista
    elif simbolo == ')':
        if len(pilha) > 0:      # len = tamanho
            pilha.pop()         # pop = remove o último elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
