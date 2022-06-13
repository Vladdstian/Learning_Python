from coffee_type import coffee

coffee_g = 100  # measured in grams
milk_ml = 200  # measured in ml
water_ml = 300  # measured in ml
money_in_machine = 0  # $

coins = {
    "pennies": 0.01,
    "dimes": 0.10,
    "nickels": 0.05,
    "quarters": 0.25,
}


def insert_coins():
    total_inserted = 0
    for items in coins:
        total_coins = int(input(f"How many {items}?: "))
        total_value = total_coins * coins[items]
        total_inserted += total_value
    return total_inserted


def check_coffee(req_coffee):
    if coffee_g < req_coffee:
        print("Sorry there is not enough water!")
        return False
    else:
        return True


def check_milk(req_milk):
    if milk_ml < req_milk:
        print("Sorry there is not enough water!")
        return False
    else:
        return True


def check_water(req_water):
    if water_ml < req_water:
        print("Sorry there is not enough water!")
        return False
    else:
        return True


def req_money(req_coins):
    print("Please insert coins.")
    money_sum = insert_coins()
    amount_not_achieved = True
    while amount_not_achieved:
        if money_sum > req_coins:
            rest = money_sum - req_coins
            print(f"Here is ${rest} in change.")
            return True
        elif money_sum < req_coins:
            to_pay = req_coins - money_sum
            print(f"You still need to pay ${to_pay}.")
            money_sum = insert_coins()
        else:
            return True


def report():
    print(f"Water: {water_ml}ml")
    print(f"Milk: {milk_ml}ml")
    print(f"Coffee: {coffee_g}g")
    print(f"Money: ${money_in_machine}")


def order():
    # Ask for choice
    global water_ml, milk_ml, coffee_g, money_in_machine
    while True:
        choice = input("What would you like to order? (espresso/latte/cappuccino) ")
        choice_price = 0
        choice_coffee = 0
        choice_milk = 0
        choice_water = 0
        if choice == "report":
            report()
        else:
            for item in coffee:
                if choice == item["type"]:
                    choice_price = item["price"]
                    choice_coffee = item["coffee"]
                    choice_milk = item["milk"]
                    choice_water = item["water"]
            req_money(choice_price)
            if check_water(choice_water):
                if check_milk(choice_milk):
                    if check_coffee(choice_coffee):
                        print(f"Here is your {choice}. Enjoy!")
                        water_ml -= choice_water
                        milk_ml -= choice_milk
                        coffee_g -= choice_coffee
                        money_in_machine += choice_price
                        continue
                    else:
                        print("The machine needs more coffee!. Please come back later!")
                        break
                else:
                    print("The machine needs more milk!. Please come back later!")
                    break
            else:
                print("The machine needs more water!. Please come back later!")
                break


# TODO 1. This is a nice feature of Pycharm
order()
