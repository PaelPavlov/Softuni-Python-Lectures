import re
text = input()

pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'

#matches = re.findall(pattern, text)
matches = re.finditer(pattern, text)
# for match in matches:
#     day = match[0]
#     #separator = match[1]
#     month = match[2]
#     year = match[3]
#     print(f'Day: {day}, Month: {month}, Year: {year}')

for match in matches:
    day = match.group(1)
    separator = match.group(2)
    month = match.group(3)
    year = match.group(4)
    print(f'Day: {day}, Month: {month}, Year: {year}')