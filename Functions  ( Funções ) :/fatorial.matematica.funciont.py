def fatorial(n, show=False):
    """
    - Calcula o fatorial de um número -
    Parameters
    ----------
    n : Inteiro,Número a ser calculado.
    show : Boolean & optional
        Mostrar ou não o calculo.
    Returns
    -------
    f : O valor do fatorial de um número do 'n'

    """
     
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c>1:
                print('x', end='')
            else:
                print('=', end='')
        f = f*c
    return f

print(fatorial(10),True)  
help(fatorial)
      