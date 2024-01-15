count_of_numbers = int(input())
even_numbers = 0
odd_numbers = 0
for numbers in range(count_of_numbers):
    current_number = int(input())
    if numbers % 2:
        even_numbers += current_number
    else:
        odd_numbers += current_number

if even_numbers == odd_numbers:
    print(f"Yes")
    print(f"Sum = {even_numbers}")
else:
    difference = abs(even_numbers - odd_numbers)
    print(f"No")
    print(f"Diff = {difference}")
