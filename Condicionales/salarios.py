print("Evaluar salarios")

presidente=int(input("Introduce el salario del Presidente: "))
print("El salario del director es: ", presidente)

director=int(input("Introduce el salario del Director: "))
print("El salario del director es: ", director)


jefe=int(input("Introduce el salario del Jefe: "))
print("El salario del director es: ", jefe)


tecnico=int(input("Introduce el salario del Tecnico: "))
print("El salario del director es: ", tecnico)

if tecnico<jefe<director<presidente:
    print("Los salarios estan bien")
else:
    print("Los salarios estan mal")