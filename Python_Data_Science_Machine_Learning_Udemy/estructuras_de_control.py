temperatura = 21

if temperatura > 16 and temperatura < 22 :
    print("El clima es agradable")

amigos = ["Juan", "Ana", "Laura"]

#nombre = input("dime un nombre: ")
nombre = "Ema"
if nombre in amigos:
    print(f"{nombre} esta en mi grupo de amigos")

temperatura = True
if temperatura:
    print("Hace calor")

    
edad = 13
if edad >= 18:
    print("Adulto")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")

x1, x2, x3 = int(input("Ingresa x1: ")), int(input("Ingresa x2: ")), int(input("Ingresa x3: "))

if x1 > x2:
    if x1 > x3:
        maximo = x1
    else:
        maximo = x3
elif x2 > x3:
    maximo = x2
else:
    maximo = x3

print("El maximo es: " + str(maximo))