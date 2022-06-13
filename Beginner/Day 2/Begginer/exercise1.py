# Write a program that adds the digits in a 2-digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_num = int(input("please give me a 2 digit number: \n"))

# solution 1 - string data change
str_two_digit_num = str(two_digit_num)
result = int(str_two_digit_num[0]) + int(str_two_digit_num[1])
print(result)

# solution 2 - more mathematics
result = two_digit_num % 10
two_digit_num -= result
result += two_digit_num / 10
print(int(result))
