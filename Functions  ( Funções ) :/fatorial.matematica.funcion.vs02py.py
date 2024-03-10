#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
#o primeiro que indique o número a calcular e outro chamado show, que 
#será um valor lógico (opcional) indicando se será mostrado ou não na 
#tela o processo de cálculo do fatorial.

def fatorial(num,show=False):
        """
        Fatorial é um cálculo matemático
        em demostrar a multiplicação descrescente
        de um número
          
        Parameters
        ----------
        num : Int - 'num' é um número inteiro
        a ser inserido pelo usuário.
        show : Boolean & optional se o usuário
        deseja ver o cálculo passo a passo
        Returns : Retorna o valor de 'num'
        com a opção de mostrar o cálculo
        -------
        """
        
        for c in range(num,0,-1):
               if show:
                print(c,end='')
                if c > 1:
                 print('x',end='')
                else:
                 print('=', end='')
            fat = fat * c
        return fat
        
num=int(input('Digite um número:'))                
show = bool(input('Deseja ver a operação??[Enter para FALSO]'))                
print(fatorial(num,show))
        
              
                                

