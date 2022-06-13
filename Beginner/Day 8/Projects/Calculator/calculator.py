# This is a calculator app
import functions

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

operations = {
    "+": functions.add_numbers,
    "-": functions.subst_numbers,
    "*": functions.multiply_numbers,
    "/": functions.divide_numbers,
    "%": functions.divide_rest
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number\n"))
    while True:
        for symbol in operations:
            print(symbol)
        op_symbol = input("Which operation would you like to do? ")
        num2 = float(input("Please pick another number\n"))
        result1 = operations[op_symbol](num1, num2)
        print(f"{num1} {op_symbol} {num2} = {result1}")

        continue_op = input("Would you like to do another operation?type 'y' to continue calculating, 'n' to start a "
                            "fresh calculation or 'q' to quit\n")
        if continue_op == 'y':
            num1 = result1
            continue
        elif continue_op == 'n':
            calculator()  # this means recursion -> a function that calls itself
        elif continue_op == 'q':
            break
        else:
            print("I don't understand what you want")
            break


calculator()
