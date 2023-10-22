As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# As listas ficam entre colchetes.
# As listas são mutáveis.
# Exemplo:

    #lanche=['hamburger','suco','pizza','pudim']
           #lanche[3]='picole'

# Para adicionar o elemento no final da lista é:
    # lanche.append('cookies')
# Para adicionar elementos em outras posições:
    # lanche.insert(0,'cachorro-quente')
        # o cachorro-quente irá para a posição zero (0)

# Para apagar dados dentro da lista é:
    # del lanche[3]

# Para eliminar de outra maneira dados da lista indicando pelo ÍNDICE:
    # lanche.pop(3)

# Outro método sem indicar pelo índice e sim pelo conteúdo:
# lanche.remove('pizza')
# Reposicionam os elementos da lista.

# Para não dar erro em remover algum elemento da lista, que não está na lista,
# por a condição 'if':
    # if 'pizza' in lanche:
     #   lanche.remove('pizza')

# É possível criar listas através de 'range':
    # valores=list(range(4,11))
    # O range cria a lista de maneira organizada e ordenada e crescente.

#  Método sort() coloca listas em desordem em ORDEM.
# exemplo:
    # valores=[8,2,5,4,9,3,0]
    # valores.sort()
      # Resultado:
          # Ele vai ordenar todos os valores: 0,2,3,4,5,8,9
    # valores.sort(reverse=True)
        # resultado será: O valor ordenado inverso.
