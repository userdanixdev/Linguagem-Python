# Gráfico de linha com Pylab:
import matplotlib.pyplot as plt
from pylab import *

# Gráfico de linhas:
# Dados:    
x = linspace(0,5,10)
y = x **2
# Cria a figura:
fig = plt.figure()
# Define a escala dos eixos:
axes = fig.add_axes([0,0,0.8,0.8])
# Cria o plot:
axes.plot(x,y,'red') 
# Labels e Título:
axes.set_xlabel('x')    
axes.set_xlabel('y')    
axes.set_title('Gráfico de linha')
-----------//-----------------//-----------------//------------------//----------------
# Criação dos 2 gráficos em uma área de plotagem:
# Dados:    
x = linspace(0,5,10)
y = x **2
# Cria a figura:
fig = plt.figure()
# Criar dois eixos principais:
axes1 = fig.add_axes([0.1,0.1,0.8,0.8]) # Eixo para figura principal
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) # Eixo para figura principal
# Figura Principal:
axes1.plot(x,y,'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')                 
axes1.set_title('Figura Principal')
# Figura Secundária:
axes2.plot(y,x,'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')                 
axes2.set_title('Figura Secundária')




