text = input()
numbers = ''
letters = ''
others = ''

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(numbers)
print(letters)
print(others)