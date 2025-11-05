import pandas as pd

data = {
    "Nombre":["Ana", "Luis", "Carlos", "Sara"],
    "Edad" : [25,30,22,27],
    "Ciudad":["Madrid", "Barcelona", "Valencia", "Bilbao"]
}

df = pd.DataFrame(data)
print(df.head())

#Agregar nueva columna a un DF
df["Salario"] = [30000,45000,38000,32000]
print(df.head())

#Cambiar contenido de una columna ya existente
df["Salario"] = df["Salario"] + 2000
print(df.head())

#Traer columna/serie y guardarla en una columna
nombre = df["Nombre"]
print(nombre)

#Filtrar DataFrames
mayores_25 = df[df["Edad"] > 25]
print(mayores_25)

str1 = "hola"
print(dir(str1))