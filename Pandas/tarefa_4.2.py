
import pandas as pd
import matplotlib.pyplot as plt

# Criação do data frame da tabela de dados
tabela_dados_df = pd.DataFrame({
    'Nome':['Pedro','Joel','Elisabete','Cristiane','Renato','Jeferson'],
     'Idade':[24,25,23,21,22,26],
      'Altura': [1.70,1.80,1.60,1.80,1.71,1.87]})  

# Mostrar a tabela:
print(tabela_dados)   

# Plot do gráfico
plt.hist([tabela_dados_df['Idade']],bins=5)
plt.title('Frequência de Idades')
plt.xlabel('Idades')
plt.ylabel('Frequência')
plt.show()
