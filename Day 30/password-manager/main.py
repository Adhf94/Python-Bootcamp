import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from pass_gen import pass_generator
import pyperclip
import json


# ----------------------MANAGE JSON-----------------------------------------------
def manage_show_list():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            dic_keys = [name for (name) in data]
        return dic_keys
    except KeyError:
        messagebox.showinfo(title="Error", message="Theres no account information. ")
    except:
        messagebox.showinfo(title="Error", message="Theres no account information. ")
    finally:
        pass


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
    new_data = {
        web: {
            "email": email,
            "password": password
        }
    }

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Website, Email or Password can't be blank.")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data.
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # writing  new data.
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data.
            data.update(new_data)
            if len(data) == 0:
                with open("data.json", "w") as data_file:
                    # Saving updated data.
                    json.dump(new_data, data_file, indent=4)
                    data.update(new_data)
            else:
                with open("data.json", "w") as data_file:
                    # Saving updated data.
                    json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="#f7f5dd")
# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="#f1f8dd")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# LABELS
website = Label(text="Website :", bg="#f7f5dd")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username :", bg="#f7f5dd")
email_username.grid(column=0, row=2)

password_label = Label(text="Password :", bg="#f7f5dd")
password_label.grid(column=0, row=3)

# ENTRYS
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=3, sticky=W)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=3, sticky=W)
email_entry.insert(0, "adhf94@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=W + E)

# BUTTONS
add_button = Button(text="Add.", width=36, command=save, background="lightgrey")
add_button.grid(column=1, row=4, columnspan=2, sticky=W + E)

generatep_button = Button(text="Generate Password.", command=generate_password, background="lightgrey")
generatep_button.grid(column=2, row=3, sticky=W)


# Manage window


def show_new_window():
    def back():
        color.destroy()
        back_button.destroy()
        list_box.destroy()
        search_button.destroy()
        delete_button.destroy()

    # def insert_value():
    #     choice = list_box.get(list_box.curselection())
    #     print(choice)
    #     back()

    def delete_acc():
        acc_to_search = str(list_box.get(list_box.curselection()))
        with open("data.json", "r") as data_file:
            new_data = json.load(data_file)

        if acc_to_search in new_data:
            del new_data[acc_to_search]
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file)
        back()

    def search_info():
        acc_to_search = list_box.get(list_box.curselection())
        print(acc_to_search)
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            password = data[acc_to_search]["password"]
            pyperclip.copy(password)
            password_entry.insert(0, password)
            website_entry.insert(0, acc_to_search)
            back()
    lista = Frame(window)
    lista.tkraise()
    color = Label(text="", bg="#f7f5dd", width=40, height=20)
    color.grid(column=0, row=0, columnspan=6, rowspan=5, sticky=W + E + S)
    back_button = Button(text="⇦", font=("arial", 19, "bold"), fg="red", command=back)
    back_button.grid(column=0, row=0, sticky=NW)

    search_button = Button(text="Search", font=("arial", 15, "normal"), background="lightgrey", command=search_info)
    search_button.grid(column=2, row=0, sticky=N + E + W)

    delete_button = Button(text="Delete", font=("arial", 15, "normal"), background="lightgrey", command=delete_acc)
    delete_button.grid(column=2, row=1, sticky=N + E + W)
    try:
        list_box = Listbox(font=("arial", 15, "bold"))
        keys = manage_show_list()
        for item in keys:
            list_box.insert(keys.index(item), item)
        list_box.bind("<<ListboxSelect>>", )
        list_box.grid(column=1, row=0, sticky=W)
    except Exception:
        pass


manage_button = Button(text="Manage.", font=24, background="lightgrey", command=show_new_window)
manage_button.grid(column=2, row=1, sticky=N + W + E, rowspan=3)
manage_button.columnconfigure(1, weight=1)

window.mainloop()
