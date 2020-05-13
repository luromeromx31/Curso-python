print("Programa para calcular la demia aritmetica de tres numeros")

num1=input("Ingresa un numero: ")
num2=input("Ingresa el segundo numero: ")
num3=input("Ingresa el último numero: ")

def media(num1,num2,num3):
    media=(num1+num2+num3)/3
    return media


resultado=media(int(num1),int(num2),int(num3))

print("La media es: ", resultado)