from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(0, nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(0, nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(0, nr_numbers)]
    # concatenate the list
    test = password_letters + password_symbols + password_numbers
    random.shuffle(test)
    # join all letters in the list with "" and converts content to a string
    password = "".join(test)
    password_entry.insert(0, string=password)
    # copy to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# function to grab website info, email address and password and save to a text file


def save_info():
    entry_test = website_entry.get()
    email_test = email_entry.get()
    password_test = password_entry.get()
    if len(entry_test) <= 0 or len(password_test) <= 0:
        messagebox.showwarning(message="Details missing", title="error")
    else:
        message_ok = messagebox.askokcancel(message=f"Confirming Website: {entry_test}\n Email: {email_test}\n "
                                                    f"Password: {password_test}\n" 
                                                    f"Is this correct?", icon="question", title='capture')
        if message_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{entry_test} | {email_test} | {password_test}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# setup background image
canvas = Canvas(width=200, height=200)
# store image in variable
padlock_image = PhotoImage(file="logo.png")
# create canvas (x-cord, y=cord, image reference
canvas.create_image(100, 100, image=padlock_image)

canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0, "testemail@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Create Password", command=generate)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
