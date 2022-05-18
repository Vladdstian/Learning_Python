from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

to_Go = CoffeeMaker()
coffee_menu = Menu()
money_printer = MoneyMachine()

while True:
    choice = input("What would you like to order? (espresso/latte/cappuccino) ")
    if choice == "report":
        to_Go.report()
        money_printer.report()
        continue
    else:
        choice = coffee_menu.find_drink(choice)
        if to_Go.is_resource_sufficient(choice):
            money_printer.make_payment(choice.cost)
            to_Go.make_coffee(choice)
        else:
            break
