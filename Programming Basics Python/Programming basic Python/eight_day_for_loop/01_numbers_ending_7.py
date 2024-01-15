
#solution 1
for num in range(1, 1001):
    if num % 10 == 7:
        print(num)

#solution 2
for num in range(7, 1001, 10):
    print(num)

