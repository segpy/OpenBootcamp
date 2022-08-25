from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

window = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(window, text="Peugeot", variable=opcion, 
            value='Peugeot', command=seleccionar).pack(anchor=W)

Radiobutton(window, text="Opel", variable=opcion, 
            value='Opel', command=seleccionar).pack(anchor=W)
Radiobutton(window, text="Renault", variable=opcion,   
            value='Renault', command=seleccionar).pack(anchor=W)
Radiobutton(window, text="Seat", variable=opcion,   
            value='Seat', command=seleccionar).pack(anchor=W)

monitor = Label(window)
monitor.pack()
Button(window, text="Reiniciar", command=reset).pack()

window.mainloop()

