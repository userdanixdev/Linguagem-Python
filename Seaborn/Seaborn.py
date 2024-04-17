!pip install seaborn
import seaborn as sea

# Carregando dados que vem no seaborn:
dados =  sea.load_dataset('tips')

# O método 'joinplot' cria plot de 2 variáveis com gráficos bivariados e univariados:
sea.jointplot(data=dados,x='total_bill',y='tip',kind='reg')

# O método lmplot() cria plot com dados e modelos de regressão:
sea.lmplot(data = dados, x = 'total_bill',y='tip', col='smoker')

## OUTRO EXEMPLO:

# Construir um Data Frame com Pandas:
df = pd.DataFrame()
# Alimentar  o DataFrame com valores aleatórios:
df['Idade']=random.sample(range(20,100),30)
df['Peso']=random.sample(range(55,150),30)
# lmplot para modelo linear:
sea.lmplot(data=df,x='Idade',y='Peso',fit_reg=True) # <- Fit_reg cria um modelo de regressão

# Gráfico de Densidade:
sea.kdeplot(df.Idade)




