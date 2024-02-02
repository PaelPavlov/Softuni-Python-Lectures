def sort_numbers(sequence):
    numbers = list(map(int, sequence.split()))
    ascending_numbers = sorted(numbers)
    return ascending_numbers

input_sequence = input()

result = sort_numbers(input_sequence)
print(result)