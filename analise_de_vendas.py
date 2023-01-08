import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

"""
upload arquivo em drive via codigo. obs.: a importação é temporária, se fechar tem de fazer novamente.
"""

from google.colab import files
arq = files.upload()

df = pd.read_excel('<caminho-nome da planilha .xlsx a ser analisada>')

# Qtd de linhas colunas
df.shape
df.head()

# Tipos de dados
df.dtypes

# Soma dos valores de venda
df['VAL VENDA'].sum()

# Cria tabela custo. qtd x custo unitário
df['Custo'] = df['QTD'].mul(df['CUSTO UNITARIO'])
df.head(1)

# Soma tabela Custo total, arredondando com 2 casas decimais.
round(df['Custo'].sum(),2)

# Lucro por peça 
df["Lucro"] = df['VAL VENDA'].mul(df['QTD']) - df['Custo']
df.head(1)


# Lucro total
df['Lucro'].sum()

# Dias em tempo de envio da mercadoria
df['Tempo Envio'] =  (df['DATA ENVIO'] - df['DATA VENDA'])
df.head(1)

# Remover, eliminar item de id 4
df.drop(4)

# Tornando 'Tempo Envio' em inteiro para calular media.
df['Tempo Envio'] =  (df['DATA ENVIO'] - df['DATA VENDA']).dt.days
df.head(1)

# Media de tempo de envio por GRUPO MARCA.
df.groupby('MARCA')['Tempo Envio'].mean()

# Analiza valores ausentes na base
df.isnull().sum()

# Lucro médio por marca e ano
df.groupby([df['DATA VENDA'].dt.year, 'MARCA'])['Lucro'].sum()

# Guarda informaçoes ACIMA em DATAFRAME.
lucro_ano = df.groupby([df['DATA VENDA'].dt.year, 'MARCA'])['Lucro'].sum().reset_index()
lucro_ano

# Total do produto vendidos.
df.groupby('PRODUTO')['QTD'].sum().sort_values(ascending=False)

# Apresentação em grafico para dados acima
df.groupby('PRODUTO')['QTD'].sum().sort_values(ascending=True).plot.barh(title='Total vendido')
plt.xlabel('Total')
plt.ylabel('Produto')

# Apresentação em grafico Lucro por ano
df.groupby(df["DATA VENDA"].dt.year)['Lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita')

# Abaixo apenas os numeros para analisar o grafico
df.groupby(df["DATA VENDA"].dt.year)['Lucro'].sum()

# Analisar apenas as vendas ano de 2010
df_2010= df[df['DATA VENDA'].dt.year == 2010]
df_2010

# Saber o lucro por mês em 2010
df_2010.groupby(df_2010['DATA VENDA'].dt.month)['Lucro'].sum().plot(title='Lucro x Mês')
plt.xlabel('Mês')
plt.ylabel('Lucro');

# Lucro por Marca e grupo
df_2010.groupby('MARCA')['Lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro');
plt.xticks(rotation='horizontal')

# Lucro por FABRICANTE
df_2010.groupby('FABRICANTE')['Lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro');
plt.xticks(rotation='horizontal')

# Dados estatisticos usando o describle em tempo de envio
round(df['Tempo Envio'].describe(),2)

# Boxplot
plt.boxplot(df['Tempo Envio']);

# Tempo minimo de envio
df['Tempo Envio'].min()

#histograma
plt.hist(df['Tempo Envio'])

# Tempo mínimo
df['Tempo Envio'].min()

# Tempo máximo
df['Tempo Envio'].max()

# Tempo igual a 16 dias
df[df['Tempo Envio'] == 16]

# Gera arquivo de analise em .csv com o nome 'Minha_analise'
df.to_csv('Minha_analise', index=False)