def min_max_numbers(sequence):
    numbers = list(map(int, sequence.split()))

    min_value = min(numbers)
    max_value = max(numbers)
    sum_values = sum(numbers)

    return min_value, max_value, sum_values


input_sequence = input()

min_val, max_val, sum_val = min_max_numbers(input_sequence)

print(f"The minimum number is {min_val}")
print(f"The maximum number is {max_val}")
print(f"The sum number is: {sum_val}")