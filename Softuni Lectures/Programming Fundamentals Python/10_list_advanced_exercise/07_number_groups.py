# def store_numbers(string_of_numbers):
#     ranges = {10: [], 20: [], 30: [], 40: [], 50: []}
#     numbers = map(int, string_of_numbers.split(", "))
#     for num in numbers:
#         for key in ranges.keys():
#             if num <= key:
#                 ranges[key].append(num)
#                 break
#     for key, value in ranges.items():
#         print(f"Group of {key}'s: {value}")

# string_of_numbers = input()
# store_numbers(string_of_numbers)


numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]