# creating graphical user interfaces

import tkinter

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=500)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack()  # it is a geometry management system

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    my_label.config(text="Button Got clicked")


button = tkinter.Button(text="click me!", command=button_clicked)
button.pack()


window.mainloop()  # it has to be at the end
