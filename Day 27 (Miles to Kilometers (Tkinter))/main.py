from tkinter import *

window = Tk()
window.title("GUI Program")


def calculate():
    miles = int(input.get())
    value_label.config(text=f"{round(miles * 0.62)}")


input = Entry(width=10)
input.grid(column=1, row=0)
input_label = Label(text="Miles")
input_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
value_label = Label(text="0")
value_label.grid(column=1, row=1)
units_label = Label(text="Km")
units_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
