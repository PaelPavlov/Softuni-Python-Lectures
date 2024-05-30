def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total

# def multiply(*args):
#     return reduce(lambda x, y: x * y, args)
print(multiply(1, 4, 5))

print(multiply(4, 5, 6, 1, 3))

print(multiply(2, 0, 1000, 5000))