print("Programa para crear un generador anidado con 'yield from'.")

def devCiudad(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
        yield from elemento

ciudadesDev=devCiudad("CDMX","Medellin","Buenos Aires","Brazilia")

print(next(ciudadesDev))
print(next(ciudadesDev))