# zeroes = [int(numbers) for numbers in input().split(", ")]

# while 0 in zeroes:
#     zeroes.remove(0)
#     zeroes.append(0)

# print(zeroes)

zeroes_as_strings = input().split(", ")

for number in zeroes_as_strings:
    number = "0"
    zeroes_as_strings.remove(number)
    zeroes_as_strings.append(number)

zeroes_as_integer = list(map(int, zeroes_as_strings))

print(zeroes_as_integer)