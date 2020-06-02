from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Usuarios")

#----------- Funciones

def salirApp():
    valor=messagebox.askquestion("Salir", "¿Desea Salir de la aplicación?")
    if valor=="yes":
        root.destroy()





#------------- Menus

fUsuarios=Frame(root, width=300, height=300)
fUsuarios.pack()

barraMenus=Menu(root)
root.config(menu=barraMenus)

DDBBMenu=Menu(barraMenus, tearoff=0)
DDBBMenu.add_command(label="Conexión")
DDBBMenu.add_command(label="Salir", command=salirApp)

borrarMenu=Menu(barraMenus, tearoff=0)

CRUDMenu=Menu(barraMenus, tearoff=0)
CRUDMenu.add_command(label="(C) Insertar")
CRUDMenu.add_command(label="(R) Leer")
CRUDMenu.add_command(label="(U) Actualizar")
CRUDMenu.add_command(label="(D) Borrar")


ayudaMenu=Menu(barraMenus, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Versión")


barraMenus.add_cascade(label="BBDD", menu=DDBBMenu)
barraMenus.add_cascade(label="Borra", menu=borrarMenu)
barraMenus.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenus.add_cascade(label="Ayuda", menu=ayudaMenu)


#----------------- Campos

labelID=Label(fUsuarios, text="ID:")
labelID.grid(column=0, row=0, sticky="e")
campoID=Entry(fUsuarios)
campoID.grid(column=1, row=0, pady=5 , padx=5)


labelNombre=Label(fUsuarios, text="Usuario: ")
labelNombre.grid(column=0, row=1, sticky="e")
campoNombre=Entry(fUsuarios)
campoNombre.grid(column=1, row=1, pady=5, padx=5)

labelPWD=Label(fUsuarios, text="PWD: ")
labelPWD.grid(column=0, row=2, sticky="e")
campoPWD=Entry(fUsuarios)
campoPWD.grid(column=1, row=2, pady=5, padx=5)

labelApellido=Label(fUsuarios, text="Apellido: ")
labelApellido.grid(column=0, row=3, sticky="e")
campoApellido=Entry(fUsuarios)
campoApellido.grid(column=1, row=3, pady=5, padx=5)

labelDireccion=Label(fUsuarios, text="Dirección: ")
labelDireccion.grid(column=0, row=4, sticky="e")
campoDireccion=Entry(fUsuarios)
campoDireccion.grid(column=1, row=4, pady=5, padx=5)

labelComentarios=Label(fUsuarios, text="Comentarios: ")
labelComentarios.grid(column=0, row=5, sticky="e")
textoComentario=Text(fUsuarios, width=20, height=10)
textoComentario.grid(column=1, row=5, pady=5, padx=5)

botonCrear=Button(fUsuarios, text="Crear")
botonCrear.grid(column=0, row=6, pady=5, padx=5)

botonLeer=Button(fUsuarios, text="Leer")
botonLeer.grid(column=1, row=6, pady=5, padx=5)

botonActualizar=Button(fUsuarios, text="Actualizar")
botonActualizar.grid(column=0, row=7, pady=5, padx=5)

botonEliminar=Button(fUsuarios, text="Eliminar")
botonEliminar.grid(column=1, row=7, pady=5, padx=5)

root.mainloop()