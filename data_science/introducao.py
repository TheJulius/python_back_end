import pandas as pd
import seaborn as sns


notas = pd.read_csv("ratings.csv")

notas.columns = ["usuarioId", "filmesId", "notas", "momento"] #como alterar o nome das colunas

print(notas.head()) #head mostra as 5 primeiras linhas

print(notas.shape) #shape mostra a quantidade de registros e a quantidade de colunas da tabela

print(notas["notas"].unique()) #como saber os valores UNICOS de uma coluna especifica

print(notas.notas.value_counts()) #como saber quantas vezes os valores aconteceram em uma coluna especifica

print("Media: ", notas["notas"].mean()) # mostra a media dos valores de uma coluna especifica

print("Mediana:", notas.notas.median()) # mostra a mediana dos valores de uma coluna especifica

print(notas.notas.describe()) #da varias informacoes e uma visao geral dos dados

print(notas.notas.plot())

print(notas.groupby("filmesId").mean()["notas"]) #agrupa por coluna especifica e faz a media

sns.boxplot(notas.notas)
sns.distplot(notas.notas)