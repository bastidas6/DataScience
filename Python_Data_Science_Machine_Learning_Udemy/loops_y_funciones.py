for item in [0,1,2,3,4,5]:
    print(item)

for letra in "python":
    print(letra)

paises = ["Argentina", "Colombia", "Perú", "México"]

for p in paises:
    largo = len(p)
    print(f"{p} tiene {largo} letras")

for p in paises:
    if len(p) > 6:
        print(f"{p} tienen nombre largo")
    else:
        print(f"{p} tienen nombre corto")

#Anidar loops
colores = ["rojo", "azul", "verde"]
prendas = ["sombrero", "pantalon", "zapato"]

for color in colores:
    for prenda in prendas:
        print(prenda, color)

ejemplo = "hueco"
print(dir(ejemplo))

#FUNCION RANGE
#Devuelve un rango de numeros

mi_rango = range(7)
for n in mi_rango:
    print(n)

mi_rango = range(5,10)
for n in mi_rango:
    print(n)
print("---------------")
mi_rango = range(5,10,2)
for n in mi_rango:
    print(n)

palabra = "python"

for n in range(len(palabra)):
    print(n)

print("loop while")

#LOOP WHILE
contador = 0

while contador < 5:
    print(contador)
    contador += 1

contador = 0
while contador <= 10:
    contador += 1
    if contador == 5:
        continue
    if contador == 8:
        break
    print(contador)

print("-----------Funciones---------------")
#FUNCIONES
def saludo():
    print("Hola esto es un saludo")
saludo()

def tu_saludo(nombre):
    print(f"Hola {nombre}, como estas?")
tu_saludo("Gilberto")

def sumar(a, b):
    resultado = a + b
    return resultado
numero = sumar(7,9)
print(numero)

def imprimir_pares_hasta(n):
    for numero in range(1, n + 1):
        if numero % 2 == 0:
            print(numero)
imprimir_pares_hasta(12)

def pedir_nombre():
    nombre = "Manuel"
    return nombre

def pedir_apellido():
    apellido = "Bastidas"
    return apellido

def saludar():
    saludo = f"Hola {pedir_nombre()} {pedir_apellido()}"
    print(saludo)

saludar()

#Ejercicio
def calcular_tablas (numero, limite):
    for i in range(1,limite + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

calcular_tablas(5,3)

def solicitar_informacion():
    numero = int(input("Ingrese el numero: "))
    limite = int(input("Ingrese el limite: "))
    calcular_tablas(numero, limite)

bandera = True
while bandera == True:
    solicitar_informacion()
    respuesta = int(input("Marque 1 si desea calcular otra tabla --- Marque 2 si desea finalizar el porgrama"))
    if respuesta == 1:
        continue
    else:
        break