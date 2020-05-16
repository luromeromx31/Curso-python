print("Programa que pide numeros positivos y los suma.")

numero=int(input("Introduce el numero a sumar: "))
suma=0

while numero>0:
    suma=suma+numero
    numero=int(input("Introduce el numero a sumar: "))

print("Se ha introducido un numero negativo")
print("la suma de los positivos es: " + str(suma))