numbers_sequence = input().split()
text = input()

message = []

for number in numbers_sequence:
    index = sum(int(digit) for digit in number)
    
    while index >= len(text):
        index -= len(text)
    
    char = text[index]
    message.append(char)
    
    text = text[:index] + text[index + 1:]

print("".join(message))