## Dois gráficos na mesma área de plotagem:
import matplotlib.pyplot
# Inserindo massa de dados :
x1 = ['Fundamental','Médio','Superior','Pós','Mestrado']
y1 = [6,7,8,2,1] 
x2 = ['Fundamental','Médio','Superior','Pós','Mestrado']
y2 = [5,10,5,2,2]
## Plotagem dos dois gráficos:
plt.bar(x1,y1,label='Ensino', color='green')
plt.bar(x2,y2,label='Ensino-2', color='blue')
plt.legend()
plt.show()
