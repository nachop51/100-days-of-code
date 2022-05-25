from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Label

label = Label(text="I am a Label", font=(
    "Cascadia Code", 24, "bold"))  # italic
# label.pack()  # expand=True makes the object expand all the possible container size
# label.place(x=100, y=100)
label.grid(column=0, row=0)

label["text"] = "New value"
label.config(text="New text", padx=20, pady=20)

# Button


def button_clicked():
    label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()


button2 = Button(text="Click me", command=button_clicked)
button2.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)
# input.pack()

window.mainloop()
