from tkinter import *

window = Tk()
window.title("Task app")
window.config(padx=50, pady=50)
# create canvas
canvas = Canvas(width=200, height=200)

task_image = PhotoImage(file="task.png")
canvas.create_image(100, 100, image=task_image)
canvas.grid(row=0, column=1, columnspan=2)

#Label
description_label = Label(text="Task description")
description_label.grid(row=1, column=1)
date_label = Label(text="Date")
date_label.grid(row=2, column=1)


# Entries
description_entry = Entry(width=35)
description_entry.grid(row=1, column=2)
description_entry.insert(0, "Enter text here")
date_entry = Entry(width=35)
date_entry.grid(row=2, column=2)
date_entry.insert(0, "format YYYY/MM/DD")

window.mainloop()
