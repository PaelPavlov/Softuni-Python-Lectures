all_strings = input().split()
total_sum = 0
for current_string in all_strings:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    current_number = int(current_string[1: len(current_string) -1])
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_number / first_letter_position
    elif first_letter.islower(): #else:
        first_letter_position = ord(first_letter) - 96
        total_sum += current_number * first_letter_position
    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower(): #else:
        last_letter_position = ord(last_letter) - 96
        total_sum +=  last_letter_position
print(f"{total_sum:.2f}")
 