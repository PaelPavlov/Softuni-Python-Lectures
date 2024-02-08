numbers_list = list(map(int, input().split(", ")))

found_evens = map(
    lambda x: x if numbers_list[x] % 2 == 0 else 'no', 
    range(len(numbers_list))
)

even_numbers = list(filter(lambda a: a != 'no', found_evens))

print(even_numbers)