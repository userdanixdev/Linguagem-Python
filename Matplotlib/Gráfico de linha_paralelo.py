# GRÁFICOS DE LINHA EM PARALELO:

import matplotlib as plt
from pylab import *
# Criação dos 2 gráficos em uma área de plotagem:
# Dados:    
x = linspace(0,5,10)
y = x **2
# Cria a figura:
fig = plt.figure()
# Dividir a área de plotagem em dois subplots:
fig,axes = plt.subplots(nrows = 1,ncols=2)
# Loop pelos eixos para criar cada plot:
for ax in axes:
    ax.plot(x,y,'r')    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')
# Ajustar o layout:
fig.tight_layout()    
