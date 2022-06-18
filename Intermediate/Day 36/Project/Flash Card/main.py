from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Create main window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create variables for images to be used separately as different functionalities
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

# Create canvas
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 265, image=back_image)
canvas.grid(row=0, column=0)


window.mainloop()
