n = int(input())

names = []

for _ in range(n):
    name = input()

    if name not in names:
        names.append(name)

print(*names, sep='\n')