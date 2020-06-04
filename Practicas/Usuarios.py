import tkinter as tk
from  tkinter import ttk
from tkinter import messagebox
import db1 as DB

root=tk.Tk()
root.title("Usuarios")

#----------- Variables

cID=tk.StringVar()
cNombre=tk.StringVar()
cPWD=tk.StringVar()
cApellido=tk.StringVar()
cDireccion=tk.StringVar()
tComentario=tk.StringVar()


tUsuarios=[
    cID.get(),
    cNombre.get(),
    cPWD.get(),
    cApellido.get(),
    cDireccion.get(),
    tComentario.get()
]

#----------- Funciones

def salirApp():
    valor=messagebox.askquestion("Salir", "¿Desea Salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    
    campoID.delete(0,tk.END)
    campoNombre.delete(0,tk.END)
    campoPWD.delete(0,tk.END)
    campoApellido.delete(0,tk.END)
    campoDireccion.delete(0,tk.END)
    textoComentario.delete(1.0, tk.END)
    
def crear():

    if cNombre.get()=="" or cPWD.get()=="" or cApellido.get()=="":
        messagebox.showerror("Falta Información", "Los campos: Nombre, Apellido y PWD son obligatorios.")
    else:
        DB.C(cNombre.get(),cPWD.get(),cApellido.get(),cDireccion.get(),tComentario.get())
    limpiarCampos()

def eliminar():

    if cNombre.get()=="":
        messagebox.showerror("Falta Información", "Solo se puede eliminar buscando por el campo: Nombre.")
    else:
        DB.D(cNombre.get())
    limpiarCampos()

def actualizar():
    usuarios=[]
    if cID.get()=="":
        messagebox.showerror("Falta Información", "Solo se puede actualizar un registro existente")
    else:
        DB.U(cNombre.get(), cPWD.get(), cApellido.get(), cDireccion.get(), tComentario.get(), cID.get())
    limpiarCampos()

def buscar():
    usuarios=[]
    if cNombre.get()=="":
        messagebox.showerror("Falta Información", "Solo se puede buscar por el campo: Nombre.")
    else:
        usuarios=DB.R(cNombre.get())
    
    cID.set(usuarios[0])
    cPWD.set(usuarios[2])
    cApellido.set(usuarios[3])
    cDireccion.set(usuarios[4])
    tComentario.set(usuarios[5])

def infoAdicional():
    messagebox.showinfo("Información", "Base de usuarios, 0.0.1_2020")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

#------------- Menus

fUsuarios=tk.Frame(root, width=300, height=300)
fUsuarios.pack()

fBotones=tk.Frame(root)
fBotones.pack()

barraMenus=tk.Menu(root)
root.config(menu=barraMenus)

DDBBMenu=tk.Menu(barraMenus, tearoff=0)
DDBBMenu.add_command(label="Crear Tabla", command=DB.iniciar)
DDBBMenu.add_command(label="Borrar Tabla", command=DB.borrarTabla)
DDBBMenu.add_command(label="Salir", command=salirApp)

borrarMenu=tk.Menu(barraMenus, tearoff=0)
borrarMenu.add_command(label="Limpiar Campos", command=lambda:limpiarCampos())

CRUDMenu=tk.Menu(barraMenus, tearoff=0)
CRUDMenu.add_command(label="(C) Insertar", command=lambda:crear())
CRUDMenu.add_command(label="(R) Leer", command=lambda:buscar())
CRUDMenu.add_command(label="(U) Actualizar", command=lambda:actualizar())
CRUDMenu.add_command(label="(D) Eliminar", command=lambda:eliminar())


ayudaMenu=tk.Menu(barraMenus, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Versión", command=infoAdicional)


barraMenus.add_cascade(label="BBDD", menu=DDBBMenu)
barraMenus.add_cascade(label="Limpiar", menu=borrarMenu)
barraMenus.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenus.add_cascade(label="Ayuda", menu=ayudaMenu)

#----------------- Campos

labelID=tk.Label(fUsuarios, text="ID:")
labelID.grid(column=0, row=0, sticky="e")
campoID=tk.Entry(fUsuarios, textvariable=cID)
campoID.grid(column=1, row=0, pady=5 , padx=5)
campoID.configure(width=30, state="readonly")

labelNombre=tk.Label(fUsuarios, text="Usuario: ")
labelNombre.grid(column=0, row=1, sticky="e")
campoNombre=tk.Entry(fUsuarios, textvariable=cNombre)
campoNombre.grid(column=1, row=1, pady=5, padx=5)
campoNombre.configure(width=30)

labelPWD=tk.Label(fUsuarios, text="PWD: ")
labelPWD.grid(column=0, row=2, sticky="e")
campoPWD=tk.Entry(fUsuarios, textvariable=cPWD)
campoPWD.grid(column=1, row=2, pady=5, padx=5)
campoPWD.configure(width=30, show="*")

labelApellido=tk.Label(fUsuarios, text="Apellido: ")
labelApellido.grid(column=0, row=3, sticky="e")
campoApellido=tk.Entry(fUsuarios, textvariable=cApellido)
campoApellido.grid(column=1, row=3, pady=5, padx=5)
campoApellido.configure(width=30)

labelDireccion=tk.Label(fUsuarios, text="Dirección: ")
labelDireccion.grid(column=0, row=4, sticky="e")
campoDireccion=tk.Entry(fUsuarios, textvariable=cDireccion)
campoDireccion.grid(column=1, row=4, pady=5, padx=5)
campoDireccion.configure(width=30)

labelComentarios=tk.Label(fUsuarios, text="Comentarios: ")
labelComentarios.grid(column=0, row=5, sticky="ne")
textoComentario=tk.Text(fUsuarios, width=20, height=10)
textoComentario.grid(column=1, row=5, pady=5, padx=5)
textoComentario.config(width=30)


# --------------- Botones

botonInsertar=tk.Button(fBotones, text="(C) Insertar", command=lambda:crear())
botonInsertar.grid(column=0, row=1, pady=5, padx=5)
botonInsertar.config(width=9)

botonLeer=tk.Button(fBotones, text="(R) Leer", command=lambda:buscar())
botonLeer.grid(column=1, row=1, pady=5, padx=5)
botonLeer.config(width=9)

botonActualizar=tk.Button(fBotones, text="(U) Actualizar", command=lambda:actualizar())
botonActualizar.grid(column=2, row=1, pady=5, padx=5)
botonActualizar.config(width=9)

botonEliminar=tk.Button(fBotones, text="(D) Eliminar", command=lambda:eliminar())
botonEliminar.grid(column=3, row=1, pady=5, padx=5)
botonEliminar.config(width=9)

root.mainloop()