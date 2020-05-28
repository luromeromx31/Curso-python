from tkinter import *

root=Tk()

miFrame=Frame(root,width=500, height=400)
miFrame.pack()

miImagen=PhotoImage(file="Grafico/navigate-right256_24872.png")
Label(miFrame, image=miImagen).place(x=100, y=100)

#miLabel=Label(miFrame, text="Hola Python")
#miLabel.place(x=100, y=200)

#miLabel=Label(miFrame, text="Hola Python", fg="red", font=("Comic Sans MS", 24)).place(x=100, y=200)



root.mainloop()