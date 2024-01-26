list_of_numbers = [int(number) for number in input().split()]
number_of_removed_numbers = int(input())

for number in range(number_of_removed_numbers):
    min_value = min(list_of_numbers)
    list_of_numbers.remove(min_value)

string_numbers = [str(number) for number in list_of_numbers]
result_string = ', '.join(string_numbers)
print(result_string)

