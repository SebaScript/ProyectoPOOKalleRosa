from tkinter import *

raiz = Tk()

raiz.title("Sistema Kalle Rosa")

raiz.geometry("1366x768")

raiz.iconbitmap("C:\\Users\\Usuario\\PycharmProjects\\ProyectoPOOKalleRosa\\resources\\logoKR.ico")

etiqueta = Label(raiz, text = "Kalle Rosa jeans", bg = "gold")

etiqueta.pack(fill = X)

boton1 = Button(raiz, text = "Si")
boton1.pack()

raiz.mainloop()

