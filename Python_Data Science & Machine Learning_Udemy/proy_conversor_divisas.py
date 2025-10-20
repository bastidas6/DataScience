nombre = "Manuel Alejandro"
fecha = "12/10/2025"
saludo = "Buenos dias"

bienvenida = saludo + " " + nombre + "! Hoy es " + fecha + ". Bienvenido al servicio de divisas!"
print(bienvenida)

dolares = 210.0
print("Dolares: " + str(dolares))
euros_a_recibir = dolares*0.88
print("Los euros a recibir son: " + str(euros_a_recibir), "para " + str(dolares) + " dolares.")

billetes_10 = euros_a_recibir // 10
billetes_1 = (euros_a_recibir - (billetes_10 * 10)) //1
monedas = euros_a_recibir - (billetes_10 * 10) - (billetes_1)
print("Billetes de 10: " + str(billetes_10) + " , Billetes de 1: " + str(billetes_1) + " , Monedas: " + str(monedas))