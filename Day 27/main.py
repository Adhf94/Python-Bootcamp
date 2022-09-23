from tkinter import *


def button_clicked():
    entry_input = input.get()
    my_label.config(text=entry_input)


window = Tk()
window.title("Mi primer GUI")
window.minsize(width=500, height=400)
window.config(padx=100,pady=200)

#Label
my_label = Label(text="text label", font=("Arial", 24, "normal"))
# EL pack, basicamente empuja el label a mostrarse en la screen.
my_label.grid(column=0, row=0)

#En tkinter podemos usar botones, formularios de entrada, y más.
#Acá una muestra de como seria usar el metodo get() en la clase Entry para poder obtener y usar la informacion escrita.
#Tambien hicimos un botón, con un nombre default, y al mismo tiempo le pasamos una funcion, que se ejecutara al momento
# de ser clicckeado.

#button
button = Button(text="button1", command=button_clicked)
button.grid(column=1, row=1)
#Entry
input = Entry(width=10)
input.grid(column=3, row=2)
#NEW BUTTON
button2 = Button(text="New Button")
button2.grid(column=2, row=0)





















window.mainloop()