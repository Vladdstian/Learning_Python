from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


#

def right_press():
    pass


def wrong_press():
    pass


# Create main window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create variables for images to be used separately as different functionalities
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Create canvas
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 265, image=back_image)
canvas.grid(row=0, column=0, columnspan=2)

# Create the buttons
right_button = Button(image=right_image, highlightthickness=0, command=right_press)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong_press)
wrong_button.grid(row=1, column=0)

window.mainloop()
