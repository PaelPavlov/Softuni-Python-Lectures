import re

line = input()

while line:
    pattern = r"\d+"
    matches = re.findall(pattern, line)
    if matches:
        print(" ".join(matches), end= " ")

    line = input()
