import math
#from numpy.lib.scimath import sqrt

print("Programa para validar numeros positivos para obtener una raíz cuadrada")

numero1=int(input("Por favor introduce un numero: "))

intentos=0

while numero1<0:
    print("No se puede calcular la raiz cuadrad de un numero negativo.")

    if intentos==2:
        print("Has consumidos demasiados intentos.")
        break;
    numero1=int(input("Por favor introduce un numero: "))
    if numero1<1:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero1)
    print("La raiz cuadrada de " + str(numero1) + " es: " + str(solucion))