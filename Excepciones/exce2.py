def divide():
    try:
        num1=float(input("Introduce el primer numero: "))
        num2=float(input("Introduce el segundo numero: "))

        print("La división es: " + str(num1/num2))
    except ValueError:
        print("Solo se reciben numeros.")
    except ZeroDivisionError:
        print("No se puede dividir entre Zero.")
    finally:
        print("Calculo finalizado")

divide()