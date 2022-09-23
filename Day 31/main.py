from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    flip_timer = window.after(3000, change_card)


def change_card():
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])


def is_known():
    to_learn.remove(current_card)
    next_card()
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)


#Ventana
window = Tk()
window.title("Flash Card APP")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, change_card)

#Cartas (CANVAS)
canvas = Canvas(width=800, height=526)
new_image = PhotoImage(file="./images/card_front.png")
old_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=new_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

#buttons
x_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=x_image, background=BACKGROUND_COLOR, highlightthickness=0,
                        borderwidth=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR,
                        activebackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0, sticky=E, padx=50)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, background=BACKGROUND_COLOR, highlightthickness=0,
                      borderwidth=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1, sticky=W, padx=50)





next_card()


window.mainloop()

