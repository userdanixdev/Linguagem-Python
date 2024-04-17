# Plotando um gráfico usando as bibliotecas utilizadas:
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
# Valores randômicos:
n = 1000
pct_smokers = 0.2
# Variáveis:
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40,10,n)
altura = np.random.normal(170,10,n)
peso = np.random.normal(70,10,n)

# Data Frame:
dados = pd.DataFrame({'altura':altura,'peso':peso,'flag_fumante':flag_fumante})
# Cria os dados para a variável flag_fumante em valores fumantes e não fumantes:
dados['flag_fumante']= dados['flag_fumante'].map({True:'Fumante',False:'Não Fumante'})

# Plotando o gráfico:
#style:
sea.set(style = 'ticks')
# LMplot:
sea.lmplot(x = 'altura',y='peso',data=dados,hue = 'flag_fumante',palette=['tab:blue',                                                                    
          'tab:orange'],height = 7)
#Labels e título:
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre altura e Peso de fumantes e não fumantes')
plt.show()
