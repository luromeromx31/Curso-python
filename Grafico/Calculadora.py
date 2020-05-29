from tkinter import *

raiz=Tk()
raiz.title("Calculadora")

miFrame=Frame(raiz)
miFrame.pack()

#-----------  Pantalla

numeroPantalla=StringVar()


pantalla=Entry(miFrame, textvariable=numeroPantalla, width=25)
pantalla.grid(row=1, column=1, columnspan=4, padx=5, pady=5)
pantalla.config(background="black", fg="blue", justify="right")

#---------- Pulsaciuones teclado

def numeroPulsado(pul):

    numeroPantalla.set(numeroPantalla.get() + pul)


#-------------  Fila 1

boton7=Button(miFrame, text="7", command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1, padx=5, pady=5)

boton8=Button(miFrame, text="8", command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2, padx=5, pady=5)

boton9=Button(miFrame, text="9", command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3, padx=5, pady=5)

botonDiv=Button(miFrame, text="/")
botonDiv.grid(row=2, column=4, padx=5, pady=6)

#-------------  Fila 2

boton4=Button(miFrame, text="4", command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1, padx=5, pady=5)

boton5=Button(miFrame, text="5", command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2, padx=5, pady=5)

boton6=Button(miFrame, text="6", command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3, padx=5, pady=5)

botonMult=Button(miFrame, text="x")
botonMult.grid(row=3, column=4, padx=5, pady=6)

#-------------  Fila 3

boton1=Button(miFrame, text="1", command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1, padx=5, pady=5)

boton2=Button(miFrame, text="2", command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2, padx=5, pady=5)

boton3=Button(miFrame, text="3", command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3, padx=5, pady=5)

botonRes=Button(miFrame, text="-")
botonRes.grid(row=4, column=4, padx=5, pady=6)

#-------------  Fila 4

boton0=Button(miFrame, text="0", command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1, padx=5, pady=5)

botonPunt=Button(miFrame, text=".", command=lambda:numeroPulsado("."))
botonPunt.grid(row=5, column=2, padx=5, pady=5)

botonRes=Button(miFrame, text="=")
botonRes.grid(row=5, column=3, padx=5, pady=5)

botonSum=Button(miFrame, text="+")
botonSum.grid(row=5, column=4, padx=5, pady=6)

raiz.mainloop()