edad=input("Introduce la edad: ")

while (edad.isdigit()==False):
    edad=input("Por favor, introduce un valor numerico: ")

if (int(edad)<18):
    print("No puedes pasar.")
else:
    print("Ya puedes pasar.")