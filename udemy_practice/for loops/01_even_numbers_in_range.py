result = 0
x = int(input())
for number in range(1, x + 1):
    if number % 2 == 0: # or we can use start 2 and step 2 in the loop range instead.
        result += number

print(result)