# Gráfico de Histograma:
import matplotlib as plt
from pylab import *
import numpy as np
# Histograma:
# Dados:    
n = np.random.randn(100000)
fig = plt.figure()
# Criação dos subplots:
fig,axes = plt.subplots(1,2,figsize = (12,4)) 
# Plot 1 :
axes[0].hist(n)
axes[0].set_title('Histograma Padrão')
axes[0].set_xlim((min(n),max(n)))
# Plot 2 :
axes[1].hist(n,cumulative = True, bins=50)
axes[1].set_title('Histograma Cumulativo')    
axes[1].set_xlim((min(n),max(n)))
