student_count = int(input())
good_grade = 0
medium_grade = 0
bad_grades = 0
extremely_bad_grade = 0
score_count = 0
score_total = 0

for _ in range(student_count):
    score = float(input())
    score_count += 1
    score_total += score
    if score >= 5.00:
        good_grade += 1
    elif score >= 4.00 and score <= 4.99:
        medium_grade += 1
    elif score >= 3.00 and score <= 3.99:
        bad_grades += 1
    elif score >= 2.00 and score <= 2.99:
        extremely_bad_grade += 1

good_grade_percentage = good_grade / student_count * 100
medium_grade_percentage = medium_grade / student_count * 100
bad_grades_percentage = bad_grades / student_count * 100
extremely_bad_grade_percentage = extremely_bad_grade / student_count * 100
average_grade = score_total / score_count

# Изход:
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
print(f"Top students: {good_grade_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {medium_grade_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {bad_grades_percentage:.2f}%")
print(f"Fail: {extremely_bad_grade_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
# Всички числа трябва да са форматирани до втория знак след десетичната запетая.
