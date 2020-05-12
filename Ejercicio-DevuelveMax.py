print("Programa para evaluar dos numeros y regresar el mayor")

num1=input("Introduce el primer numero: ")
num2=input("Introduce el segundo numero: ")

def max(num1, num2):
    if num1<num2:
        print("El numero mayor es: ",num2)
    elif num2<num1:
        print("El numero mayor es: ",num1)
    else:
        print("Los numeros son iguales")

max(int(num1),int(num2))