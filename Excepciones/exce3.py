def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas")
    elif edad<20:
        return("Eres muy Joven")
    elif edad<40:
        return("Eres Joven")
    elif edad<65:
        return("Eres Maduro")
    elif edad<100:
        return("Cuudate")

edad=int(input("Introduce tu edad: "))

print(evaluaEdad(edad))