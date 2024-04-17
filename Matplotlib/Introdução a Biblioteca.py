!pip install matplotlib
import matplotlib.pyplot as plt
%matplotlib inline  <<- Comando Jupyter Notebook
plt.plot([1,3,5],[2,4,7])
plt.show()
-------//------------//----------------//----------------//

#Outro exemplo:
# Criar as variáveis - Massa de dados
x=[2,3,5]
y=[3,5,7]
# Ponha os títulos PRINCIPAL, EIXO X E Y:
plt.plot(x,y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
-----------------//--------------------//------------------//----------

