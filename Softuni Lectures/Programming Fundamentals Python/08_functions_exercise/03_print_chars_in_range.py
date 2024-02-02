def chars_range(first_char, second_char):
    result = ''

    for i in range(ord(first_char) + 1, ord(second_char)):
        result += chr(i) + ' '

    return result

char1 = input()
char2 = input()
print(chars_range(char1, char2))