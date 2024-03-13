import re
names = input()
valid_names = []

regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(regex, names)

for name in matches:
    print(name, end=' ')