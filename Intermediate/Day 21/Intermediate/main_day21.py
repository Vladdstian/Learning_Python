# Inheritance and list slicing

# Inheritance
# Class inheritance is another feature of OOP
# It is basically a process of inheriting behaviour and appearance from another existing class
# when taking about class inheritance, both appearance and behaviors can be inherited
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale")


class Fish(Animal):  # Fish is a class derived from Animal class
    def __init__(self):
        super().__init__()  # takes all attributes from the super class = Animal class

    def breath(self):  # methods from the inherited class can be overridden
        super().breath()  # if we still want to use the original method but improve upon it, we have to call it first
        print("doing it underwater")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breath()  # it can use methods from the inherited class
nemo.swim()  # it can also use methods form its own class
