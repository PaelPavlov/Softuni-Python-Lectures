import math

number_of_students = int(input())
number_of_lectures = int(input())
bonus = int(input())
highest = 0

for student in range(number_of_students):
    student_attendence = int(input())
    if student_attendence == highest:
        continue
    if student_attendence > highest:
        highest = student_attendence


total_bonus = highest / number_of_lectures * (5 + bonus)

print(f"Max Bonus: {math.ceil(total_bonus)}.")
print(f"The student has attended {math.ceil(highest)} lectures.")

