import pandas as pd
df = pd.read_csv(r"C:\Users\manue\OneDrive\Documents\DataScience\Python_Data_Science_Machine_Learning_Udemy\PANDAS\recursos\Top-Películas.csv")
pd.set_option("display.max_columns", None)

print(df.head())
print("-----------------------------------------------------------")
print(df.tail())
print("-----------------------------------------------------------")
print(df.info())
print("-----------------------------------------------------------")
print(df.describe())
print("-----------------------------------------------------------")

#Ordenacion de DataFrames
#Proceso de organizar los datos en un orden especifico para facilitar la visualizacion y el analisis

df_ordenado = df.sort_values(["rating", "recaudación(M)"], ascending=False) #De mayor a menor
print(df_ordenado.head(10))

#Agrupar datos

#Agrupar promedio de ganancias por genero
df_agrupado = df.groupby("género")["rating"].mean()
print(df_agrupado)

df_agrupado_2 = df.groupby("año")["recaudación(M)"].sum()
df_agrupado_2 = df_agrupado_2.sort_values(ascending=False)
print(df_agrupado_2.head(10))