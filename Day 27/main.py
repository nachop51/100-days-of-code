from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Label

label = Label(text="I am a Label", font=("Cascadia Code", 24, "bold"))  # italic
label.pack()  # expand=True makes the object expand all the possible container size

label["text"] = "New value"
label.config(text="New text")

# Button


def button_clicked():
    label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()


window.mainloop()
