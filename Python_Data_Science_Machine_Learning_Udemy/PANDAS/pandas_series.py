import pandas as pd 

df = pd.read_csv(r"C:\Users\manue\OneDrive\Documents\DataScience\Python_Data_Science_Machine_Learning_Udemy\PANDAS\recursos\Precipitaciones.csv")
print(df.head())

#Una serie es un arreglo unidimensional
serie = df.region 
print(serie.head())

#Convertir una lista en series de pandas
datos = [10,20,30,40,50]
serie2 = pd.Series(datos)

print(serie2)

#Asignar indices personalizados a la serie
indices = ["a","b", "c", "d","e"]
serie3 = pd.Series(datos, indices)
print(serie3)

#Traer algun indice
valor = serie3["b"]
print(valor)

print(type(serie3))
print(type(serie3["b"]))

#Asignar serie desde un diccionario
capitales = {"España": "Madrid", "Perú": "Lima", "Argentina": "Buenos Aires"}
serie4 = pd.Series(capitales)
print(serie4)

print(serie4["Perú"])

###OPERACIONES BASICAS - SERIES
serie5 = pd.Series([10,20,30,40,50])
serie5[0] = serie5[0] + 10
print(serie5)

#Suma a todos los valores de serie un valor de 10
serie5 = serie5 + 10
print(serie5)

#Multiplicar todos los valores de la seri por 5
serie5 = serie5 * 5
print(serie5)