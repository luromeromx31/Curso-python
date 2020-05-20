print("Programa para capturar la excepción al dividir por 0")

def divide(num1,num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

while True:
    try:
        num1=int(input("Introduce un numero: "))
        num2=int(input("Introduce el segundo numero: "))
        break
    except ValueError:
        print("Solo se pueden introducir numeros, intente denuevo")
    
    
try:
    divide(num1,num2)
except NameError:
    print("Un valor no fue introducido.")