from tkinter import *

root=Tk()

root.title("Ejemplo de Check Button")

playa=IntVar()
montana=IntVar()
tRural=IntVar()

def opcionesViaje():
    opcionEscojida=""

    if(playa.get()==1):
        opcionEscojida+=" Playa"
    elif(montana.get()==1):
        opcionEscojida+=" Montaña"
    elif (tRural.get()==1):
        opcionEscojida+=" Turismo Rural"
    textoFinal.config(text=opcionEscojida)

foto=PhotoImage(file="Grafico/navigate.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige Destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=tRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()