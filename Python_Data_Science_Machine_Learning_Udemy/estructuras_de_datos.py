#LISTAS
#Las listas son una coleccion de objetos
#Las listas son mutables, cambia el objeto, NO me genera una copia
#En cambio los strings son inmutables, siempre hacen los cambios es a una copia, el string sigue igual.
#Los metodos que salen con: "__x__" son metodos que no son exclusivos del elemento, puede usarse en otros elementos

frutas = ["banana","fresa", "manzana"]
print(type(frutas))

mis_listas = [[10,20,30],["a", "b", "c"], ["Pablo", "Micaela", "Milena"]] #Lista de listas
print(type(mis_listas))

print(mis_listas[0]) #Llamar un elemento de la lista
print(mis_listas[2][1]) #Llamar a un elemento de una lista dentro de otra lista

frutas[0] = "sandia" #Asignar un elemento
print(frutas)

frutas.append("mamoncillo") #Añadir un elemento
print(frutas)

frutas.sort() #Ordena en orden alfabetico
print(frutas)

frutas.sort(reverse=True) #Ordena en orden alfabetico pero de atras para adelante
print(frutas)

frutas.remove("manzana") #Eliminar un elemento de la lista
print(frutas)

frutas.reverse() #Me devuelve la lista al reves
print(frutas)

#print(dir(frutas)) #Metodos de la lista frutas
print(len(frutas))

#Concatenacion de listas
lista1 = [1,2,3]
lista2 = [4,5,6]
combinada = lista1+ lista2
print(combinada)

#Repetir listas
repetida = lista1 * 3
print(repetida)

#Segmentar listas
sublista = combinada[1:4]
print(sublista)



#TUPLAS
#Son una estrucutura de dtaos,una coleccion de elementos ordenados y no modificables, la tupla una vez creada no pueden cambiar sus elementos y su tamaño
#Las tuplas son colecciones inmutables

t = 1, 2
print(type(t))

tt = (1,2)
print(type(tt))

tm = ("Manuel", "Bastidas", 27)
print(type(tm))

mi_tupla = (1,2,3,2,2,4)
elemento = mi_tupla[2]
print(elemento)

sub_tupla = mi_tupla[1:3]
print(sub_tupla)

primer_elemento, segundo_elemento = t
print(segundo_elemento)

#Tupla de tuplas
nacimiento = (1985, 12,10)
nombre = ("Juan", "Pérez")
cliente = (nombre, nacimiento)
print(cliente)
print(type(cliente))

#DICCIONARIOS
#Se caracteriza por ser una coleccion de elementos, y cada elemento se componen de una clave y de un valor, no puede haber valor sin clave y viceversa y las claves deben ser unicas
#Los diccionarios no se pueden indexar, ya que no son secuencias ordenadas, por eso no se pueden encontrar por un indice, se debe hallar es por clave

dic = {}
print(type(dic))

edades = {"Juan": 25, "Maria": 32}
print(len(edades))

print(edades["Juan"]) #me devuelve 25

edades["Juan"] = 34
print(edades["Juan"])

edades["Laura"] = 11
print(edades)

print(edades.keys())

print(edades.values())

print(edades.items())

print(edades.get("Juan"))

edades.update({"Juan":27})

print(edades.items())

#BOOLEANOS
#Solo puede tener dos valores posibles: verdadero o falso

a = True
print(type(a))

x = 2
y = 5
comparar = x == y

print(comparar)

#Operadores booleanos and, or y not
z = 8
comparar = x < y and y < z
print(comparar)

otra = not comparar #Comparar no es verdadera? = comparar es falsa?
print(otra)