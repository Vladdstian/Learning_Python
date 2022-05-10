# write a program that calculates the average student height from a List of heights.
# without using count() and sum()

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_students = 0
total_height = 0

for height in student_heights:
    total_height += height
    total_students += 1

result = round(total_height / total_students)

print(result)
