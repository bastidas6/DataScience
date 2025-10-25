#Si no se limpian los datos, se pueden contaminar los resultaods de nuestros analisis
#La mayoria de datos vienen de fuentes externas y a aveces la informacion viene con datos duplicados, con errores, sin informacion, etc
#Manejo de datos faltantes o nulos, datos inapropiados, eliminacion de duplicados

import pandas as pd 
data = {"Id_producto": [1001, 1002, 1003, 1003], "Cantidad_vendida": [30, None, 25, 25], "Precio": [20.5, 15.0, None, 22.5]}

df = pd.DataFrame(data)
print(df)

print("----------------------HEAD---------------------")
print(df.head())

#Se ven que hay dos series que tienen datos nulos, como los identificamos?
print("----------------------INFO----------------------")
print(df.info())

#Identificacmos los valores nulos con isnull()
print("----------------------NULOS----------------------")
print(df.isnull())
print("----------------------SUMAR NULOS POR SERIE-----------")
print(df.isnull().sum())

print("-----------HACER ALGO CON LOS VALORES NULOS--------------")
#Hay que hacer algo con esos valor nulos, las opciones son:
print("-------------1. ELIMINAR------------------")
#1. Eliminar registros que tienen valores faltantes
df_eliminados = df.dropna()
print(df_eliminados)

print("------------2. RELLENAR------------------")
#2. Rellenar los valores faltantes
valores_nuevos = {"Cantidad_vendida": 0, "Precio": df["Precio"].mean()}
df_rellenados = df.fillna(valores_nuevos)
print(df_rellenados)

print("--------------CORRECCIÓN DE TIPO DE DATOS--------------------") #A veces los tipos de datos no son los apropiados, por eso toca adecuarlos de acuerdo a nuestras necesidades
#Vamos a cambiar cantidad_vendida de float a entero
df_rellenados["Cantidad_vendida"] = df_rellenados["Cantidad_vendida"].astype(int)
print(df_rellenados)

print("--------------ELIMINAR DUPLICADOS--------------------")
df_unicos1 = df_rellenados.drop_duplicates() #Si no pongo parametros busca registros completos (todas las columnas exactamente iguales) iguales.
print("Sin parametros: " + str(df_unicos1))
df_unicos2 = df_rellenados.drop_duplicates(subset="Id_producto") #Siempre deja el primero
print("Con parametros: " + str(df_unicos2))