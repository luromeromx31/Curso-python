print("programa para validar numeros introducidos incrementales")

nuevo=int(input("Introduce un numero: "))
viejo=0

while nuevo>viejo:
    viejo=nuevo
    nuevo=int(input("Introduce un numero mayor que: " + str(viejo) + ":"))

print("El numero: " + str(nuevo) + " es menor que: " + str(viejo) + ", fin del programa.")