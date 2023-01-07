import tkinter

# create a window
window = tkinter.Tk()
# create a title
window.title("My Tkinter Window")
# specify a window size (width, height)
window.minsize(width=500, height=500)
# specify a label (text"", font(Font type, font size))
my_label = tkinter.Label(text="I am a label", font=("Arial", 25))
# initialise the label. defaults to top position
my_label.pack()



# remains at the very end of the program to continue to display window
window.mainloop()
