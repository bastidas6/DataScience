#Si no se limpian los datos, se pueden contaminar los resultaods de nuestros analisis
#La mayoria de datos vienen de fuentes externas y a aveces la informacion viene con datos duplicados, con errores, sin informacion, etc
#Manejo de datos faltantes o nulos, datos inapropiados, eliminacion de duplicados

import pandas as pd 
data = {"Id_producto": [1001, 1002, 1003, 1003], "Cantidad_vendida": [30, None, 25, 25], "Precio": [20.5, 15.0, None, 22.5]}

df = pd.DataFrame(data)
print(df)