# creating graphical user interfaces

import tkinter

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=500)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack(side="left")  # it is a geometry management system

window.mainloop()  # it has to be at the end

# Advanced Python arguments

# keyword arguments
# def my_function(a,b,c):
#   do this with a
#   then do this with b
#   finally do this with c

# keyword arguments with default values
# all the arguments are optional and when you want to call the function you are not required to provide any of them
# def my_function(a=1,b=2,c=3):
#   do this with a
#   then do this with b
#   finally do this with c

# functions that can take any number of arguments
# def add(*args):  -> this function takes as many arguments as you want.
# the * is very important and args is just a naming convention that all python devs might use it
# for n in args:
#   print(n)
# Example: playground add function

# functions that can take any number of key-word arguments
# Example: playground calculate function