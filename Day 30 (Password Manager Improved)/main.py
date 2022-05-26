import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- SEARCH FUNCTION ------------------------------- #


def search():
    web = web_input.get()
    print(web)
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if web in data:
                email = data[web]["email"]
                password = data[web]["password"]
            else:
                messagebox.showerror(
                    "Error", f"Website not found")
                return
        file.close()
    except:
        print("Can't open data.json")
    else:
        messagebox.showinfo(f"{web}", f"Email: {email}\nPassowrd: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():

    web = web_input.get()
    user = user_input.get()
    password = password_input.get()

    new_data = {
        web: {
            "email": user,
            "password": password,
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showwarning(
            "Oops!", "Please don't leave any fields empty!")
        return
    elif len(password) < 6:
        messagebox.showwarning("Oops!", "Password too short!")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
    except Exception:
        data = new_data
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    file.close()
    web_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_input = Entry()
web_input.grid(column=1, row=1, sticky="EW")
web_input.focus()

web_button = Button(text="Search", command=search)
web_button.grid(column=2, row=1, sticky="EW")

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2, sticky="EW")
user_input.insert(0, "nachoperalta0@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

password_button = Button(text="Generate Password", command=gen_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
