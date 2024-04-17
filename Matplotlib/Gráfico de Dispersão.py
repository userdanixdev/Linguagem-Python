# Scatter plot para analisar bi-variadas:

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]
plt.scatter(x,y, label = 'Pontos',color = 'black',marker='+')
plt.legend()
