from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Read data
try:
    data = pd.read_csv("data/french_words.csv")
except FileNotFoundError:
    data = pd.read_csv("data/words_to_learn.csv")
# Convert dataframe to list of dictionaries
words_to_learn = data.to_dict(orient="records")
# global dictionary to store French and English word
word = {}

# ------ Random word -----#
def random_word():
    global word
    global timer
    # reset timer every time you click on a button
    window.after_cancel(timer)
    word = random.choice(words_to_learn)
    # access global dictionary to access French word
    french_word = word["French"]
    canvas.itemconfig(card_title, text=f"French", fill="black")
    canvas.itemconfig(card_word, text=f"{french_word}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    # runs the timer
    timer = window.after(3000, change_card)


def is_known():
    words_to_learn.remove(word)
    new_data = pd.DataFrame(words_to_learn)
    new_data.to_csv("data/words_to_learn.csv")
    random_word()

def change_card():
    # access global dictionary to access equivalent English word
    english_word = word["English"]
    # change background color
    canvas.itemconfig(canvas_image, image=card_back_image)
    # change title text and color
    canvas.itemconfig(card_title, text=f"English", fill="white")
    # change word to English word and change color to white
    canvas.itemconfig(card_word, text=f"{english_word}", fill="white")


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# create canvas
canvas = Canvas(width=800, height=526)
# change card after set time
timer = window.after(3000, change_card)


# create front card image reference file
card_front_image = PhotoImage(file="images/card_front.png")
# create back card image reference file
card_back_image = PhotoImage(file="images/card_back.png")
# create image with x and y co-ordinate
canvas_image = canvas.create_image(400, 263, image=card_front_image)
# create text with x and y co-ordinate, text, font sty[e, size, style and assign to variable in order to edit
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
correct_image = PhotoImage(file="images/right.png")
known_btn = Button(image=correct_image, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)

incorrect_image = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=incorrect_image, highlightthickness=0, command=random_word)
unknown_btn.grid(row=1, column=0)

random_word()

window.mainloop()
