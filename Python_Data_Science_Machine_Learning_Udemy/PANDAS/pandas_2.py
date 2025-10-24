#Ejemplo con archivo de precipitaciones en las distintas provincias de españa en el año

import pandas as pd #importamos pandas
df = pd.read_csv(r"C:\Users\manue\OneDrive\Documents\DataScience\Python_Data_Science_Machine_Learning_Udemy\PANDAS\recursos\Precipitaciones.csv") #Leemos el CSV
print(type(df))

#Head - Metodo
#Tail - Metodo
print("------------------------HEAD-----------------------")
print(df.head()) #Me devuelve las primeras 5 lineas de mi DataFrame
print("------------------------TAIL-----------------------")
print(df.tail()) #Me devuelve las ultimas 5 registros por defecto de mi DataFrame

#Shape -- Atributo me devuelve el numero de filas y luego el numero de columnas
#Shape -- Atributo no lleva parentesis por que es un atributo, cuando es un metodo si lleva los parentesis
print("------------------------TAMAÑO DF-----------------------")
print(str(df.shape)) 

#Columns -- Atributo, me devuelve los encabezados de mi DataFrame, o sea el nombre de las columnas
print("------------------------COLUMNAS-----------------------")
print(str(df.columns))

#Info -- Metodo, QUE ME DEVUELVE: INFORMACION SOBRE EL DATA FRAME:
# # numero de indices 
# # el numero de columnas
# # cuantos objetos no vacios tiene cada columna 
# # que tipo de dato tiene cada columna
print("------------------------INFORMACION-----------------------")
print(str(df.info()))

#Describe -- Metodo, me trae informacion sobre las columnas NUMERICAS: promedio, moda, max, etc
print("------------------------DESCRIBE-----------------------")
print(str(df.describe()))





