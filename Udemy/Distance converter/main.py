from tkinter import *

window = Tk()

window.title("Mile to KM converter")
window.minsize(width=250, height=250)
window.config(padx=50, pady=50)

# specify a label (text"", font(Font type, font size))
mile_label = Label(text="Mile", font=("Arial", 12))
mile_label.grid(row=0, column=2)

km_label = Label(text="KM", font=("Arial", 12))
km_label.grid(row=1, column=2)

is_equal_label = Label(text="Is equal to", font=("Arial", 12))
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0", font=("Arial", 12))
result_label.grid(row=1, column=1)

mile_entry = Entry(width=5)
mile_entry.grid(row=0, column=1)


def calculate():
    my_integer = float(mile_entry.get())
    result = round(my_integer*1.609, 2)
    result_label.config(text=f"{result}")


calc_button = Button(text="Calculate", font=("Arial", 12), command=calculate)
calc_button.grid(row=2, column=1)


# remains at the very end of the program to continue to display window
window.mainloop()

