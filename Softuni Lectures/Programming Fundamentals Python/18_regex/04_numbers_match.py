import re
numbers = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

result = re.finditer(pattern, numbers)

for match in result:
    print(match.group(), end=' ')