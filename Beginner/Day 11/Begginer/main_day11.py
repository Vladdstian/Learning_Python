# Debugging: Find and fix errors inside the code

# Steps to identify a bug

# 1. Describe Problem
# def my_function():
#     for i in range(1, 20):  # 2. range function will go up until 19 and not 20
#         # 3. to solve the issue we need to update the range function to (1, 21)
#         if i == 20:  # 1. here is an assumption that 'i' will definitely reach 20
#             print("You got it")
# my_function()

# 2. Reproduce the Bug - When does the error happen?
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)  # randint returns a random value between 1 and 6, includes both end points
# dice_num = randint(0, 5)  # this solves all issues
# print(dice_imgs[dice_num])
# print(dice_imgs[6])  # Error always happens when the random function returns 6 - there is no index 6 in dice_imgs

# 3. Play Computer
# year = int(input("What's your year of birth?"))
# if 1980 < year < 1994:
#     print("You are a millennial.")
# elif year > 1994:  # here there is a logical or mistyped error - the cases don't cover the 1994 year and the code does
#     # nothing when inputted this option
#     print("You are a Gen Z.")

# 4. Fix the Errors
# age = input("How old are you?")  # The error here is: taking input as string anc comparing it with a number below
# if age > 18:  # TypeError: '>' not supported between instances of 'str' and 'int'
# print("You can drive at age {age}.")  # IDE will underline the print with red because it expects an indent
# the print statement above should be an 'f' string

# 5. Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)  # this returns the input given by the user
# word_per_page == int(input("Number of words per page: "))  #
# print(word_per_page)  # this returns 0 because the upper statement is a comparison and not an assignment
# total_words = pages * word_per_page
# print(total_words)

# 6. Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)  # using a debugger we can watch the program run line by line and see where we have the
#     # error in thinking. Solution: indent the line 50 to be underneath the 'for' loop
#     print(b_list)
#
# mutate([1, 2, 3, 5, 8, 13])


# Tips for debugging
# 7. Take a break
# 8. Ask somebody to look over
# 9. Run the code often - after every execution
# 10. StackOverflow
