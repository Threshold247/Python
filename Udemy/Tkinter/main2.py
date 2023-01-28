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
my_label.grid(column=0, row=0)
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
my_button.grid(column=1, row=1)


# Input field

my_input = Entry()
my_input.grid(column=2, row=0)

# single line entry box

my_entry = Entry(width=30)
# insert text into the box
my_entry.insert(END, string=" A text box")
print(my_entry.get())
my_entry.grid(column=3, row=2)







# remains at the very end of the program to continue to display window
window.mainloop()
