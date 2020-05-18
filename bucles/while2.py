print("Programa para introducir la edad con: While")

edad=int(input("Por favor introduce tu edad: "))

i=2
maxerr=3
while ((edad<0 or edad>100) and i<=maxerr):
    print("Has introducido una edad incorrecta. vuelve a intentar. ")
    edad=int(input("Por favor introduce tu edad: "))
    #print(i)
    i=i+1

if i>maxerr:
    print("Has introduccido demasiadas veces, tu edad es incorrecta.")
else:
    print("Gracias por participar. La edad es correcta")
    print("Fin del programa.")