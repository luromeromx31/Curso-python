import sqlite3

miConexion=sqlite3.connect("BBDD/PrimeraBase")

miCursor=miConexion.cursor()



miCursor.execute("SELECT * FROM productos WHERE seccion='Deportes'")

productos=miCursor.fetchall()
print(productos)

miCursor.execute("UPDATE productos set precio=20 where id='1'")


miCursor.execute("SELECT * FROM productos WHERE seccion='Deportes'")
productos=miCursor.fetchall()
print(productos)

miCursor.execute("DELETE FROM productos where id='1'")

miCursor.execute("SELECT * FROM productos WHERE seccion='Deportes'")
productos=miCursor.fetchall()
print(productos)


miConexion.commit()

miConexion.close()