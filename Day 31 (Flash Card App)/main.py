from msilib.schema import File
from tkinter import *
import pandas
from random import choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
# Globals
data_file = {}
current_card = {}

try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except Exception:
    data_file = pandas.read_csv("data/french_words.csv")
    data_list = data_file.to_dict(orient="records")
else:
    data_list = data_file.to_dict(orient="records")

# ---------------------------- GENERATE WORD ------------------------------- #


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data_list)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(
        word_text, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- SAVE WORD ------------------------------- #


def is_known():
    data_list.remove(current_card)
    df = pandas.DataFrame(data_list)
    df.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(
        word_text, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_background, image=card_back)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(
    400, 150, text="French", fill="black", font=LANGUAGE_FONT)
word_text = canvas.create_text(
    400, 263, fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, bg=BACKGROUND_COLOR, command=generate_word)
wrong.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, bg=BACKGROUND_COLOR, command=is_known)
right.grid(column=1, row=1)

generate_word()

window.mainloop()
