names = set()

for _ in range(int(input())):
    names.add(input())

for name in names:
    print(name)

# print(*names, sep='\n') different print by unpacking 