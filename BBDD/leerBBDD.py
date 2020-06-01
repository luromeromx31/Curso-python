import sqlite3

miConexion=sqlite3.connect("BBDD/PrimeraBase")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM productos WHERE codigo ='1'")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    print("Nombre del producto: ", producto[1], "Precio: ", producto[2], "Nombre Departamento: ", producto[3])

miConexion.commit()

miConexion.close()