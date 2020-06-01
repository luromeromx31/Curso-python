import sqlite3

miConexion=sqlite3.connect("BBDD/PrimeraBase")

miCursor=miConexion.cursor()

miCursor.execute("DROP table productos")

miCursor.execute('''
    CREATE TABLE productos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre varchar(50) UNIQUE, 
        precio integer, 
        seccion varchar(20)
        )
    
    ''')


#miCursor.execute("INSERT INTO productos VALUES('Balón', 15, 'Deportes')")

variosProductos=[
    ("Balón", 8, "Deportes"),
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 25, "Cerámica"),
    ("Camión", 345, "Jugetes"),
    ("Camiones", 34, "Jugetes")
]

miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", variosProductos)

miConexion.commit()

miConexion.close()