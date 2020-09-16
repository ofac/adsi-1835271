from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Ingresar Nombre: ")

def myClick():
	hello   = "Hola: " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()

myButton = Button(root, text="Adicionar Nombre", command=myClick)
myButton.pack()


root.mainloop()

