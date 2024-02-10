secret_message = input().split()
decipher_message = []

for word in secret_message:
    list_number = []
    list_letter = []
    for element in word:
        if element.isdigit():
            list_number.append(element)
        elif element.isalpha():
            list_letter.append(element)
    first_letter = chr(int(''.join(list_number)))
    list_letter[0],list_letter[-1] = list_letter[-1],list_letter[0]
    another_letter = ''.join(list_letter)
    print(first_letter+another_letter, end=' ')


# message = input().split()

# words = []
# for word in message:
#     num, let = "", ""
#     for symbol in word:
#         if symbol.isdigit():
#             num += symbol
#         else:
#             let += symbol
#     if len(let) != 1:
#         let = f"{let[-1]}{let[1:-1]}{let[0]}"
#     words.append(f"{chr(int(num))}{let}")

# print(*words, end=' ')