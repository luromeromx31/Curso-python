import sqlite3
from tkinter import messagebox

vError=False

def conexion():
    miConexion=sqlite3.connect("Practicas/Base.sqlite3")
    miCursor=miConexion.cursor()

def iniciar():
    vError=False
    miConexion=sqlite3.connect("Practicas/Base.sqlite3")
    miCursor=miConexion.cursor()

    conexion()

    try:
        miCursor.execute('''
        CREATE TABLE usuarios (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre varchar(50) UNIQUE,
            PWD varchar(8),
            Apellido varchar(50), 
            direccion varchar(50), 
            comentario varchar(20)
            )
        
        ''')
    except sqlite3.OperationalError:
        vError=True
        
    miConexion.commit()
    miConexion.close()
    if vError:
        messagebox.showinfo("Creación de tabla", "La tabla ya existe.")
    else:
        messagebox.showinfo("Cereación de tabla", "La tabla fue creada con éxito.")
    

def borrarTabla():
    miConexion=sqlite3.connect("Practicas/Base.sqlite3")
    miCursor=miConexion.cursor()
    miCursor.execute("DROP table usuarios")
    miConexion.commit()
    miConexion.close()
    messagebox.showinfo("Borrado de tabla", "La tabla fue borrada")

def C(campoNombre, campoPWD, campoApellido, campoDireccion, campoComentario):
    vError=False
    miConexion=sqlite3.connect("Practicas/Base.sqlite3")
    miCursor=miConexion.cursor()
    InsertUsuario=[campoNombre, campoPWD, campoApellido, campoDireccion, campoComentario]

    try:
        miCursor.execute("INSERT INTO usuarios VALUES (NULL,?,?,?,?,?)", InsertUsuario)
    except sqlite3.OperationalError:
        vError=True
    except sqlite3.IntegrityError:
        vError=True

    miConexion.commit()
    miConexion.close()

    if vError:
        messagebox.showinfo("Insertado", "La tabla NO fue actualizada")
    else:
        messagebox.showinfo("Insertado", "Los datos se guardarón")

def R(nombre):
    vError=False
    miConexion=sqlite3.connect("Practicas/Base.sqlite3")
    miCursor=miConexion.cursor()
    InsertUsuario=[nombre]
    try:
        miCursor.execute("SELECT * FROM usuarios WHERE nombre=?", InsertUsuario)
    except sqlite3.OperationalError:
        vError=True
    except sqlite3.IntegrityError:
        vError=True
    except TypeError:
        vError=True

    usuarios=miCursor.fetchone()

    return usuarios

    miConexion.close()

    if vError:
        messagebox.showinfo("Busqueda", "La datos NO se encontrarón")
    else:
        messagebox.showinfo("Busqueda", "Los datos se recuperarón")

def U(nombre, pwd, apellido, direccion, comentario, idu):
    vError=False
    miConexion=sqlite3.connect("Practicas/Base.sqlite3")
    miCursor=miConexion.cursor()
    InsertUsuario=[nombre, pwd, apellido, direccion, comentario, idu]
    try:
        miCursor.execute("UPDATE usuarios SET nombre=?, pwd=?, apellido=?, direccion=?, comentario=? where id=?", InsertUsuario)
    except sqlite3.OperationalError:
        vError=True
    except sqlite3.IntegrityError:
        vError=True
    except TypeError:
        vError=True

    miConexion.commit()
    miConexion.close()

    if vError:
        messagebox.showinfo("Actualización", "La datos NO se Actualizarón")
    else:
        messagebox.showinfo("Actualización", "Los datos se Actualizarón")

def D(nombre):
    vError=False
    miConexion=sqlite3.connect("Practicas/Base.sqlite3")
    miCursor=miConexion.cursor()
    InsertUsuario=[nombre]
    try:
        miCursor.execute("DELETE FROM usuarios where nombre=?", InsertUsuario)
    except sqlite3.OperationalError:
        vError=True
    except sqlite3.IntegrityError:
        vError=True

    miConexion.commit()
    miConexion.close()

    if vError:
        messagebox.showinfo("Insertado", "La tabla NO fue actualizada")
    else:
        messagebox.showinfo("Insertado", "Los datos se borrarón")
