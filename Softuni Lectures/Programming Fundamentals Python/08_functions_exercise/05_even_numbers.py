def filter_even_numbers(sequence):
    numbers = list(map(int, sequence.split()))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    return even_numbers


input_sequence = input()


result = filter_even_numbers(input_sequence)
print(result)