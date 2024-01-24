n = int(input())
word = input()
strings = []

for _ in range(n):
    items = input()
    strings.append(items)
print(strings)

for i in range(len(strings) -1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)

print(strings)