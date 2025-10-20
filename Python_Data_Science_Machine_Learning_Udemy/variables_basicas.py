#Variables númericas
numero1 = 5
numero2 = 8
suma = numero1 + numero2
print(suma)

#Variables tipo texto
texto = "El libro: 'el principito' es emocionante"
print(texto)

texto1 = 'viva python'
texto2 = "Viva python"
son_iguales = texto1 == texto2
print(son_iguales)

#Funcion Type, cada tipo de dato tiene sus propios metodos, ahi es donde se usa el type que me sirve para saber de que tipo de dato es.
#Todos creen que la programacion se trata de funciones fantasticas pero no, la programacion se trata de tipos de datos.
a = 1
b = "1"
print(type(a))
print(type(b))

'''En python existen 3 tipos de datos númericos -- 
int = Numeros enteros negativos y positivos, incluso el 0 
float = Números decimales
complex = numeros complejos, por fuera de los reales, en python se reemplaza la i por j'''

print(type(-7))
print(type(3.6))
print(type(-5.2 + 4J))
numero_complejo = complex(3,4)
print(numero_complejo)
numero_complejo2 = complex(2,2)
print("el tipo de: " + str(numero_complejo2) + " es: "+ str(type(numero_complejo2)))


#Operaciones matematicas en python +, -, *, /, //, %, **
print("Suma: " + str(2+2))
print("Resta: " + str(5-1))
print("Multiplicacion: " + str(8*0.5))
print("Division: " + str(10/3))
print("Division al piso: " + str(10//3)) #Devuelve el numero entero sin los decimales
print("Modulo: " + str(10%3))
c = 3 + 5j
d = 2 + 5j
print(str(c+d))
print("Potencia: " + str(5**2))
print("Raiz: " + str(25**(1/3)))