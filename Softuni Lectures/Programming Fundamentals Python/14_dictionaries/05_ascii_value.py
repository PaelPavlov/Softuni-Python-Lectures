
letter = input()


ascii_dict = {char: ord(char) for char in letter.split(", ")}

print(ascii_dict)
