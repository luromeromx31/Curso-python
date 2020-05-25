from io import open

archivo_texto=open("io/archivo.txt", "r+") #Lectura y escritura


listaTexto=archivo_texto.readlines()

listaTexto[1]="Esta es la tercer linea."

archivo_texto.seek(0)

archivo_texto.writelines(listaTexto)

archivo_texto.close()