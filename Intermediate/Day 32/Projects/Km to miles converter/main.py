from tkinter import *


def km_to_miles():
    km = float(kilometers_inputs.get())
    miles = round(km / 1.609)
    miles_result_label.config(text=f"{miles}")


window = Tk()
window.title("Kilometers to Miles converters")
window.config(padx=20, pady=20)

kilometers_inputs = Entry(width=7)
kilometers_inputs.grid(column=1, row=0)

kilometers_label = Label(text="Kilometers")
kilometers_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_result_label = Label(text="0")
miles_result_label.grid(column=1, row=1)

miles_label = Label(text="M")
miles_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=km_to_miles)
calculate_button.grid(column=1, row=2)

window.mainloop()
