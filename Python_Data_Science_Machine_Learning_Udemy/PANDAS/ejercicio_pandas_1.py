import pandas as pd

df = pd.read_csv(r"C:\Users\manue\OneDrive\Documents\DataScience\Python_Data_Science_Machine_Learning_Udemy\PANDAS\recursos\medallas.csv")

print("------------------PRIMERAS FILAS -------------------")
print(df.head())

print("------------------ULTIMAS FILAS -------------------")
print(df.tail())

print("------------------TAMAÑO DEL DATAFRAME -------------------")
print(df.shape) #93 FILAS (empezando desde 0) y 5 columnas

print("------------------COLUMNAS-------------------")
print(df.columns) 

print("------------------INFO DEL DF-------------------")
print(df.info()) 

print("------------------DESCRIPCION DEL DF-------------------")
print(df.describe()) 

#LIMPIEZA DE DATOS

print("----------------------SUMAR NULOS POR SERIE/COLUMNA-----------")
print(df.isnull().sum())

#Como se dejaron unas celdas vacias las vamos a cambiar por 0
df.fillna(0,inplace=True)


#Cambiamos el numero de medallas de float a int
df["Oro"] = df["Oro"].astype(int)
df["Plata"] = df["Plata"].astype(int)
df["Bronce"] = df["Bronce"].astype(int)

print("------------------PRIMERAS FILAS -------------------")
print(df.head())

#ANALISIS DE MEDELLA DE ORO POR PAIS
top_3_oro = df.sort_values("Oro", ascending=False).head(3)
print("Los tres primeros en oro son: \n" + str(top_3_oro))

#ANALISIS DE MEDALLAS TOTALES POR PAIS
filtro = df["Total"] > 10
analisis = df[filtro].sort_values("Total", ascending=True)
print("El medallero es: \n" + str(analisis))