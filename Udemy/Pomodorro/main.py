from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
# def reset_timer():
#     canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps

    work_seconds = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    reps += 1
    if reps % 8 == 0:
        countdown(long_break_sec)
    elif reps % 2 == 0:
        print(reps)
        countdown(short_break_sec)
    else:
        countdown(work_seconds)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    # convert into minutes rounding down
    count_minute = math.floor(count/60)
    # convert into seconds
    count_second = count % 60
    # adjusting format for seconds
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    # starting the timer
    if count > 0:
        window.after(100, countdown, count-1)
    # resetting the timer
    else:
        start_count()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=50, bg=YELLOW)
text = "✔"

# setup background image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# store image in variable
tomato_image = PhotoImage(file="tomato.png")
# create canvas (x-cord, y=cord, image reference
canvas.create_image(100, 112, image=tomato_image)
# create text on image (x-cord, y-cord, text, text color, font(font type, font size, bold/italic))
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)


my_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
my_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=start_count)
start_button.grid(row=2, column=0)

checkmark_label = Label(text=text, bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, "bold"), highlightthickness=0) # command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()

