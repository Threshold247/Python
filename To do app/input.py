import tkinter.scrolledtext
from tkinter import *
from database import Database

window = Tk()
window.title("Task app")
window.config(padx=50, pady=50)
# create canvas
canvas = Canvas(width=200, height=200)

task_image = PhotoImage(file="Image/task.png")
canvas.create_image(100, 100, image=task_image)
canvas.grid(row=0, column=0, columnspan=2)
my_database = Database()

def clear_description(event):
    description_entry.delete("0", "end")


def clear_date(event):
    date_entry.delete("0", "end")


#Label
description_label = Label(text="Task description")
description_label.grid(row=1, column=0)
date_label = Label(text="Date")
date_label.grid(row=2, column=0)
reminder_label = Label(text="Reminder")
reminder_label.grid(row=3, column=0)

# Entries
description_entry = Entry(width=35)
description_entry.grid(row=1, column=1)
description_entry.insert(0, "Enter text here")
# bind left mouse click to clear text
description_entry.bind('<Button-1>', clear_description)
date_entry = Entry(width=35)
date_entry.grid(row=2, column=1)
date_entry.insert(0, "format YYYY/MM/DD")
# bind left mouse click to clear text
date_entry.bind('<Button-1>', clear_date)

# Checkbox
add_reminder = Checkbutton()
add_reminder.grid(row=3, column=1)

# Button
add_task = Button(bg="red", text="Add task")
add_task.grid(row=4, columnspan=2)

# Scroll bar
scroll_bar = tkinter.scrolledtext.ScrolledText(width=35,  height=10)


# Listbox
listbox = Listbox(window, width=35)
my_list = my_database.get_data()
count = 0
for item in my_list:
    count += 1
    description = item[1]
    date = item[2]
    listbox.insert(count, f"{description}: {date}")
listbox.grid(row=5, columnspan=3)




window.mainloop()
