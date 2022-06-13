# creating graphical user interfaces

import tkinter

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=500)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack(side="left")  # it is a geometry management system

window.mainloop()  # it has to be at the end
