#Pandas
#Es una biblioteca que agrega funcionalidades a Python para la manipulacion y analisis de datos.
#Se utiliza principalmente para la limpieza de datos, analisis exploratorio y visualizacion de datos estadisticos.
#Simplifica los datos para enfocarnos en el analisis
#Pandas es el excel de python

import pandas as pd #Pandas ya esta instalado, pero se debe importar en el entorno de trabajo para usarlo en el codigo de python

#TIPOS DE DATOS EN PANDAS
#Series: Son las columnas de mi tabla
#DataFrame: Es la tabla de datos

datos = {"nombre": ["Pedro", "Juan", "Lorena"], "edad": [25,39,33]}
print(datos)

df = pd.DataFrame(datos) #Me crea una tabla
print(df)
print(type(df)) #Es un tipo: DataFrame

#Tenemos dos series: La serie: nombre y la serie: edad
print(df["nombre"]) #Me muestra la serie: nombre
print(df.nombre) #Me muestra tambien la serie: nombre

print(df["edad"]) #Me muestra la serie: edad
print(df.edad)#Me muestra tambien la serie: edad

print(type(df.nombre)) #Es un tipo: Serie




datos = {"nombre": ["Ana", "Luis", "Carlos"], "edad":[30,25,40]}

df_empleados = pd.DataFrame(datos)
print(df_empleados)

shape_df = df_empleados.shape
columns_df = df_empleados.columns
index_df = df_empleados.index

print(shape_df)
print(columns_df)
print(index_df)