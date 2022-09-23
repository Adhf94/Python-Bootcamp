from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global marks, reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    marks = ""
    title_timer.config(text="TIMER", font=(FONT_NAME, 60, "normal"), fg=GREEN, bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def star_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_timer.config(text="BREAK", font=(FONT_NAME, 60, "normal"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_timer.config(text="BREAK", font=(FONT_NAME, 60, "normal"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        title_timer.config(text="WORK", font=(FONT_NAME, 60, "normal"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_seg = count % 60
    if count_seg < 10:
        count_seg = f"0{count_seg}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global marks
        star_timer()
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP -------------------------------
#window FRAME
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Canvas for image and bg color
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=3, row=3)

#Labels & buttons
title_timer = Label(text="TIMER", font=(FONT_NAME, 60, "normal"), fg=GREEN, bg=YELLOW)
title_timer.grid(column=3, row=0)

check_marks = Label(text="", font=("Arial", 20, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(column=3, row=4)

button1 = Button(text="Start", fg=PINK, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=star_timer)
button1.grid(column=0, row=4)

button2 = Button(text="Reset", fg=PINK,  font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
button2.grid(column=5, row=4)




















window.mainloop()