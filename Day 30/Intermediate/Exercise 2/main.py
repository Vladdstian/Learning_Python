# list comprehension exercise
# create a second list with the even numbers of the ones in the list provided

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
