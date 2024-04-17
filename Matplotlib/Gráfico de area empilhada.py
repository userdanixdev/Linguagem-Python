# Gráfico de área empilhada :
import matplotlib.pyplot as plt
# Massa de dados:
x = [1,2,3,4,5]
y = [5,2,4,5,6]
z = [9,8,7,6,5]
n = [7,8,7,2,2]
u = [8,5,7,9,8]
plt.stackplot(x,y,z,n,u,  #<--- Variáveis declaradas acima
              colors=['m','c','r','k','b'])   #<-- LISTSA DE CORES
plt.show()
