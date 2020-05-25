from io import open

archivo_texto=open("io/archivo.txt", "w")

frase="Estupendo dia para estudiar python"

archivo_texto.write(frase)

archivo_texto=open("io/archivo.txt", "r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)