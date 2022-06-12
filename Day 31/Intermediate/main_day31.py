# Dictionary comprehension
# new_dict = {new_key:new_value for item in list} / ... if test}
# new_dict = {new_key:new_value for (key, value) in dict.items()} / ... if test}
import random
import pandas

names = ["Alex", "Beth", "Vlad", "Dave", "Eleanor", "Freddie", "Caroline"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)  # giving the head of the table
    print(value)  # each value in the table

# Loop through rows using pandas
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
