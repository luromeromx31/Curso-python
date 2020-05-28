from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=300, height=200)
miFrame.pack()

miNombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1, pady=5, padx=5)
cuadroNombre.config(fg="red", justify="center")
#cuadroTexto.place(x=90, y=100)

cuadroPwd=Entry(miFrame)
cuadroPwd.grid(row=1, column=1)
cuadroPwd.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroEdad=Entry(miFrame)
cuadroEdad.grid(row=3, column=1)

textoComentario=Text(miFrame, width=20, height=10)
textoComentario.grid(row=4, column=1, pady=5, padx=0)


scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")



textoComentario.config(yscrollcommand=scrollVert.set)

labelNombre=Label(miFrame, text="Nombre: ")
#nombreLabel.place(x=20, y=100)
labelNombre.grid(row=0, column=0, sticky="e", pady=5, padx=5)

labelPwd=Label(miFrame, text="PWD: ")
labelPwd.grid(row=1, column=0, sticky="e", pady=5, padx=5)

labelApellido=Label(miFrame, text="Apellido: ")
labelApellido.grid(row=2, column=0, sticky="e", pady=5, padx=5)

labelEdad=Label(miFrame, text="Edad: ")
labelEdad.grid(row=3, column=0, sticky="e", pady=5, padx=5)

labelTexto=Label(miFrame, text="Comentario: ")
labelTexto.grid(row=4, column=0, sticky="e", pady=5, padx=5)

def codigoBoton():
    miNombre.set("Luis")

botonEnvio=Button(raiz, text="enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()