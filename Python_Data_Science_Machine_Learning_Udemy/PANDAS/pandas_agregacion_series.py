import pandas as pd 
numeros = pd.Series([10,20,30,40,50])
print(numeros)

#AGREGACIONES MAS COMUNES

#Promedio
promedio = numeros.mean()
print("El promedio es: " + str(promedio))

#Suma
total = numeros.sum()
print(f"La suma de los valores es {total}")

#Maximo
maximo = numeros.max()
print(f"El valor maximo es: {maximo}")

#Minimo
minimo = numeros.min()
print(f"El valor minimo es: {minimo}")