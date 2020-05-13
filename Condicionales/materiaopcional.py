print("Asignaturas optativas 2017")
print("Informatica gáfica (Inf) - Pruebas de software (Pru)- Usabilidad (Usa)")

opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("inf","pru","usa"):
    print("La asifnatura elegida es: "+asignatura)
else:
    print("Asignatura no valida")