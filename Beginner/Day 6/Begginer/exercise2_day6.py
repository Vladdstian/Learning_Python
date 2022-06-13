# write a function that checks whether if the number passed into it is a prime number or not.
import math


def prime_checker(number):
    prime = True
    for nr in range(2, math.ceil(math.sqrt(number))):
        if number % nr == 0:
            prime = False
            break
    print("prime" if prime else "not prime")


n = int(input("Check this number: "))
prime_checker(number=n)
