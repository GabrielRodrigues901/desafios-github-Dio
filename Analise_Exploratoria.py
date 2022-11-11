import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#Upload de arquivos
from google.colab import files
arq = files.upload()

#Criando data frame
df = pd.read_excel("AdventureWorks.xlsx")

#Visualizando as primeiras 5 linhas
df.head()

#Qualidade de linhas e colunas
df.shape

#Verificando tipos de dados
df.dtypes

#Valor total da receita
df["Valor Venda"].sum()

#Custo total
df['Custo'] = df["Custo Unitário"].mul(df["Quantidade"])
df.head()
round(df["Custo"].sum(),2)

#Lucro
df["Lucro"] = df["Valor Venda"] - df["Custo"]

#Lucro total
round(df["Lucro"].sum(),2)

#Tempo de envio
df["Tempo de envio"] = df["Data Envio"]-df["Data Venda"]

#Extraindo os dias
df['Tempo de envio'] = (df['Data Envio'] - df['Data Venda']).dt.days
df.head(1)

#Verificando o tipo
df['Tempo de envio'].dtype

#Media de tempo de envio por Marca
df.groupby('Marca')['Tempo de envio'].mean()

#Valores Vazios
df.isnull().sum()

#Agrupando Lucro por ano por Marca
df.groupby([df['Data Venda'].dt.year,'Marca'])['Lucro'].sum()
pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o Index
lucro_ano = df.groupby([df['Data Venda'].dt.year,'Marca'])['Lucro'].sum().reset_index()
lucro_ano

#Total de Produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

#Grafico total de produtos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title="Total de produtos vendidos")
plt.xlabel("Total")
plt.xlabel("Produto")