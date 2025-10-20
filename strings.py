palabra = "manzana"
print(type(palabra))
Mayus = palabra.upper()
Capitalize = palabra.capitalize()

#dir = me muestra todos los metodos a los que se puede acceder desde una variable
#help me ayuda a darme contexto sobre para que sirve una funcion o metoro
print(dir(palabra))

#Se puede acceder a un metodo de dos formas diferentes
print(help(palabra.capitalize))
print(str.capitalize(palabra))

#indexar: Se empieza a contar caracteres desde el 0
print(palabra[0])
print(palabra[-1]) #me toma el ultimo caracter del string
print(palabra[0:5]) #Me toma los caracteres desde el 0 hasta el 4
print(palabra[4:]) #Me toma los valores desde el 4 hasta el ultimo - puedo poner un indice que se desfase del tamaño
print(palabra[::2]) #Me toma los caracteres intercalados, desde el comienzo hasta el indice 5 saltando de a 2

#Filtrar strings
palabra = "banana"
print(palabra.count("a"))
print(palabra.strip().count(" ") + 1) #Cantidad de palabras

#INPUT: Sirve para recibir mensajes por parte del usuario
mensaje = input("Dime tu nombre")
print("Hola " + mensaje)

##Formateo de string
saludo = "hola"
nombre = "Ana"
edad = 30
frase = saludo + " " + nombre
print(frase)

frase = "hola {} tienes {} años".format(nombre, edad)
print("La frase es: " + frase)

frase2 = f"Hola {nombre}, tienes {edad} años"
print("La frase 2 es: "+ frase2)

##Actividad
texto = "este curso es de python para datascience"
print("Numero total de caracteres: " + str(len(texto)))
print("Caracteres sin contar el espacio: " + str(len(texto) - texto.count(" ")))
print("Cantidad de vocales:" + str(texto.count("a")+ texto.count("e") + texto.count("i") + texto.count("o") + texto.count("u")))
print("Numero de palabras: " + str(texto.count(" ") + 1))

primer_espacio = texto.find(" ") #Indice en el que se encuentra el primer espacio
print("Sin la primera palabra: " + texto[primer_espacio+1:])

print("Reemplazar espacion por guin medio: " + texto.replace(" ", "-"))

print("Cambio de mayusculas a minusculas y viceversa: "+ texto.swapcase())