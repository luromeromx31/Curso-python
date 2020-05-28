from tkinter import *

raiz=Tk()

raiz.title("Primera ventana")
#raiz.resizable(True,False)
#raiz.iconbitmap("Navigate.ico")
raiz.geometry("650x350")
raiz.config(bg="blue")
miFrame=Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width=650, height=350)
#miFrame.pack(side="right", anchor="n")
#miFrame.pack(fill="y", expand=True)
#miFrame.pack(fill="both", expand=True)
miFrame.config(bd=5)
#miFrame.config(relief="groove")
miFrame.config(relief="sunken")
#miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")


raiz.mainloop()
