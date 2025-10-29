import pandas as pd

#Filtrado de series: Hacerle preguntas especificas a nuestros datos

serie = pd.Series([5,10,15,20,25])
print(serie)

#FILTRADO DE NUMEROS

#Cuales elementos de mi serie son mayore a un numero especifico
filtro = serie > 15 #Filtro me queda con valores booleanos que cumplen con la condicion
print("Tipo de filtro: " + str(type(filtro)) + "Filtro: \n" + str(filtro))

#Filtramos la serie que cumplan con el filtro
serie_filtrada = serie[filtro] 
print("Serie filtrada")
print(serie_filtrada)

# FILTRADO DE STRINGS

serie_2 = pd.Series(["Melon", "Banana", "Papaya"])
print(serie_2)
print(type(serie_2))

filtro_2 = serie_2.str.contains("Melon")
print(filtro_2)
serie_filtrada = serie_2[filtro_2]
print(serie_filtrada)










