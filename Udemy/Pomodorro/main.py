from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=50, bg=YELLOW)

# setup background image
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
# store image in variable
tomato_image = PhotoImage(file="tomato.png")
# create canvas (x-cord, y=cord, image reference
canvas.create_image(100, 112, image=tomato_image)
# create text on image (x-cord, y-cord, text, text color, font(font type, font size, bold/italic))
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.pack()



window.mainloop()

