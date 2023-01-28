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

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton

def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    print(fruits.index(item))
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
# remains at the very end of the program to continue to display window
window.mainloop()
