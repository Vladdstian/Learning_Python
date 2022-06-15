import tkinter.messagebox
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
    tkinter.messagebox.askokcancel(title=website, message=f"These are the login details entered:\n"
                                                          f"Email: {email}\n"
                                                          f"Password: {password}\n"
                                                          f"Is it ok to save?")
    website_entry.delete(0, END)
    pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
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
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "vlad.c.nichifor@gmail.com")
pass_entry = Entry(width=17)
pass_entry.grid(row=3, column=1)

# Buttons
gen_pass = Button(text="Generate Password")
gen_pass.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
