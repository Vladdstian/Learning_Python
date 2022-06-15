from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)
email_entry = Entry(width=17)
email_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password")
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
