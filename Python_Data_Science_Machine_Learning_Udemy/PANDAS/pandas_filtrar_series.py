print("ejemplo")
import pandas as pd 
datos = {"Pais": ["Noruega", "Colombia"], "Habitantes": [23,45]}
print(type(datos))

df = pd.DataFrame(datos)
print(df.head())

print(df.notnull().sum())