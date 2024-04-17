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
# Outro exemplo:
# Criar as variáveis com a massa de dados
x2 = [5,7,9]
y2 = [11,12,13]
# Composição dos gráficos:
plt.plot(x2,y2,label='Gráfico com Matplotlib')
plt.legend()
------------//---------------//-----------------//----------------//

