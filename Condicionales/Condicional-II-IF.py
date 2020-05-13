print("Programa para evaluar la edad")

edad=input("Por favor introduce tu edad: ")

def menor_edad(edad):
    if edad<19:
        valoracion="Eres menor, no puedes pasar"
        pass
    elif edad<25:
            valoracion="Eres Joven, Ya puedes pasar"
    elif edad<35:
            valoracion="Eres Adulto joven, Ya puedes pasar"
    elif edad<45:
            valoracion="Eres Adulto, Ya puedes pasar"
    elif edad<55:
            valoracion="Eres Mayor, Ya puedes pasar"
    else:
            valoracion="La edad no es correcta"
    pass
    return valoracion

print(menor_edad(int(edad)))