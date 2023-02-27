from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# create canvas
canvas = Canvas(width=800, height=526)
# create front card image reference file
card_front_image = PhotoImage(file="images/card_front.png")
# create image with x and y co-ordinate
canvas.create_image(400, 263, image=card_front_image)
# create text with x and y co-ordinate, text, font ty[e, size, style
canvas.create_text(400, 150, text="Text", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_image = PhotoImage(file="images/right.png")
known_btn = Button(image=correct_image, highlightthickness=0)
known_btn.grid(row=1, column=1)

incorrect_image = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=incorrect_image, highlightthickness=0)
unknown_btn.grid(row=1, column=0)



window.mainloop()
