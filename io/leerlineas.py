from io import open

archivo_texto=open("io/archivo.txt", "r")

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])

archivo_texto=open("io/archivo.txt", "a")

archivo_texto.write("\nEsta es la segunda linea")
archivo_texto.close()

print(lineas_texto[4])
print(lineas_texto[4])
