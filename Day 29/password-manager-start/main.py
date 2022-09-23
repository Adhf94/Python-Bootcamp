from tkinter import *
from tkinter import messagebox
from pass_gen import pass_generator
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password = pass_generator()
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Website, Email or Password can't be blank.")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered  \n Email: {email} "
                                                 f"\n Password: {password} \nIt's ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} : {email} : {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#LABELS
website = Label(text="Website :")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username :")
email_username.grid(column=0, row=2)

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

#ENTRYS
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=3, sticky=W+E)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=3, sticky=W+E)
email_entry.insert(0, "adhf94@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=W+E)

#BUTTONS
add_button = Button(text="Add.", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W+E)

generatep_button = Button(text="Generate Password.", command=generate_password)
generatep_button.grid(column=2, row=3, sticky=W)


























window.mainloop()

