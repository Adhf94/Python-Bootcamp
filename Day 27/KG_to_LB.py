from tkinter import *


def get_entry():
    num = int(entry.get())
    return num


def converter(state):
    value = state
    print("converter,state", state)
    num1 = get_entry()
    if value == 1:
        num1 *= 2.20462262185
        print("kg")
        print(num1)
        nom_result.config(text="LBs")
        return round(num1)
    elif value == 2:
        num1 *= 0.453592
        print("lb")
        print(num1)
        nom_result.config(text="KGs")
        return round(num1)


def show_calculate():
    radio_state = radio_used()
    total = converter(radio_state)
    print(total)
    print("show_calculate")
    label3.config(text=total)



window = Tk()
window.title("Convertidor KG-LB")
window.minsize(width=350, height=100)
window.config(padx=20, pady=20)
#LABELs
label1 = Label(text="Cantidad a calcular :", font=("Arial", 9, "normal"))
label1.grid(column=0, row=0)

label2 = Label(text="Es igual a : ", font=("Arial", 9, "normal"))
label2.grid(column=0, row=3)

label3 = Label(text=0, font=("Arial", 9, "normal"))
label3.grid(column=2, row=3)

white_space = Label(text=". ")
white_space.grid(column=4, row=0)


nom_result = Label(text="", font=("Arial", 9, "normal"))
nom_result.grid(column=4, row=3)

#Entry
entry = Entry(width=15)
entry.grid(column=3, row=0)
#boton
button = Button(text="calcular. ", command=show_calculate)
button.grid(column=5, row=3)


#Radio button

def radio_used():
    state = radio_state1.get()
    return state


radio_state1 = IntVar()
radiobutton1 = Radiobutton(text="KGs", value=1, variable=radio_state1, command=radio_used)
radiobutton2 = Radiobutton(text="LBs", value=2, variable=radio_state1, command=radio_used)
radiobutton1.grid(column=5, row=0)
radiobutton2.grid(column=5, row=2)



window.mainloop()