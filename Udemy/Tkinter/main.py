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

# single line entry box

my_entry = Entry(width=30)
# insert text into the box
my_entry.insert(END, string=" A text box")
print(my_entry.get())
my_entry.pack()

# text box

my_textbox = Text(width=50, height=8)
# place cursor in box
my_textbox.focus()
my_textbox.insert(END, " A multi line text box")
# get the text from the multi line box
print(my_textbox.get("1.0", END))
my_textbox.pack()

# Create a spinbox


def spin_input():
    print(my_spinbox.get())


my_spinbox = Spinbox(from_=0, to=10, width= 10, command=spin_input)
my_spinbox.pack()

# remains at the very end of the program to continue to display window
window.mainloop()
