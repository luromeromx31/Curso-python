edad=input("Introduce la edad: ")
edad=int(edad)

def funcname(edad2):
    if 0<edad2<100:
        print("La edad es correcta")
    else:
        print("La edad es incorrecta")

funcname(edad)