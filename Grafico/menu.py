from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Juan", "Procesador de textos versión 2018")

def avisoLicencia():
    messagebox.showwarning("Procesador de Juan", "Producto bajo licencia GNU")

def salirAplicacion():
    valor=messagebox.askquestion("salir", "¿desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def cancelAplication():
    valor=messagebox.askokcancel("Cancelar", "Desea Terminar la aplicación?")
    if valor==True:
        root.destroy()

def CerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")

def mensajeError():
    messagebox.showerror("Prueba de error", "Este es el mensaje de error")
   

barraMenu=Menu(root)

root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=CerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Mensaje de Error", command=mensajeError)
archivoHerramientas.add_command(label="Cancelar Aplicación", command=cancelAplication)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()