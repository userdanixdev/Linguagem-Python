'''Professor Gustavo Guanabara - Curso em video - Python
Variáveis compostas: Tuplas
- Armazenam vários valores ou apenas 1 em uma mesma estrutura acessíveis por chaves
individuais.
Exemplo: - strings são variáveis compostas - um nome são vários caracteres'''

#len - função de comprimento, irá ler a quantidade que possui dentro da tupla.
# tupla é entre parênteses ()
# lista é entre colchetes []
# dicionário é entre chaves {}
lanche=('hamburger','suco','pizza','pudim','batata-frita')
            #0         1      2       3          4
'''for c in lanche:
    print(c)'''

# Toda vez que fazer o looping a função 'for' irá selecionar um de cada vez.    
# Para não excluir o dado que estava na memória inbutido é importante criar uma tupla.

#print(lanche[1]) - ''' Colocar o elemento em evidência entre COLCHETES '''
                    #'''O elemento não receberá chamada com parênteses'''

#print(lanche[-3])

# Forma 1:
for comida in lanche:
        print(f'Eu vou comer {comida}')
print('Comi muito')
print(len(lanche))

Resultado:
    Eu vou comer hamburger
Eu vou comer suco
Eu vou comer pizza
Eu vou comer pudim
Eu vou comer batata-frita
Comi muito
5
 #_________________________________________________________   

# Forma 02:
for cont in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[cont]}na posição {cont}')

Resultado:
    Eu vou comer hamburgerna posição 0
 Eu vou comer sucona posição 1
 Eu vou comer pizzana posição 2
 Eu vou comer pudimna posição 3
 Eu vou comer batata-fritana posição 4
        
# Forma 03:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')

Resultado:

    Eu vou comer hamburger na posição 0
Eu vou comer suco na posição 1
Eu vou comer pizza na posição 2
Eu vou comer pudim na posição 3
Eu vou comer batata-frita na posição 4
Comi pra caramba

    
# UMA FUNÇÃO INTERESSANTE:
    # Método 'SORTED' = NÃO Mudou,não altera. A função põe na ordem alfabética 
print(sorted(lanche))

Resultado:

    ['batata-frita', 'hamburger', 'pizza', 'pudim', 'suco']

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Tuplas distintas de varíáveis compostas fazem JOIN, uma junção.
#Exemplo:
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)

Resultado:
    (5, 8, 1, 2, 2, 5, 4)

#__________________________________________________________    

        









