# creating graphical user interfaces
import tkinter


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# window creation and properties
window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack()  # it is a geometry management system
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=200) -> 1 method of positioning
my_label.grid(column=0, row=0)


# Button
button = tkinter.Button(text="click me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=20)
# input.pack()  -> cannot be mixed with grid in the same program
input.grid(column=2, row=2)

window.mainloop()  # it has to be at the end
