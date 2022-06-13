# this program will calculate the exact sum that each person has to pay (including tip) for any type of bill
print("Welcome to the tip calculator.")
total_bill = float(input("what was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? "))
total_people = int(input("How many people will split the bill? "))

tip_in_currency = tip_percentage/100 * total_bill
bill_with_tip = tip_in_currency + total_bill
person_pay = bill_with_tip/total_people

print("\n")
print(f"The tip for the ${total_bill} bill is ${tip_in_currency}.")
print(f"The total amount to pay now with a {tip_percentage}% tip is now ${bill_with_tip}")
print(f"Each person should pay: ${person_pay:0.2f}")
