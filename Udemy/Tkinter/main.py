# import entire tkinter library
from tkinter import *


# create a window
window = Tk()
# create a title
window.title("My Tkinter Window")
# specify a window size (width, height)
window.minsize(width=500, height=500)

# Making a label
# specify a label (text"", font(Font type, font size))
my_label = Label(text="I am a label", font=("Arial", 25),background="yellow")
# initialise the label. defaults to top position
my_label.pack()
# changes text 2 options
my_label["text"] = "New text"
my_label.config(text="Change Text")


# Making a button


def click():
    new_text = my_input.get()
    my_label.config(text=new_text)
    my_label.config(background="blue")

# create the button


my_button = Button(text="I am a button", command=click)
# initialise the button on screen
my_button.pack()


# Input field

my_input = Entry()
my_input.pack()


# remains at the very end of the program to continue to display window
window.mainloop()
