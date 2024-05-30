# def repeat_word(n, word):
#     for _ in range(5):
#         print(word)

# repeat_word(5, "Hello")
#################################
# def sum_nums(num1, num2):
#     return num1 + num2

# result = sum_nums(5, 4)
# print(result)
#################################

# def sum_nums(num1, num2, *args):
#     total = num1 + num2
#     for num in args:
#         total += num
#     return total

# print(sum_nums())


# def kwargs_example(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} -> {value}")

# kwargs_example(name="Peter", age=29, town="Plovdiv")


def sum_nums(num1, num2, *args, **kwargs):
    total = num1 + num2
    for num in args:
        total += num
    for key, value in kwargs.items():
        print(f"{key} -> {value}")
    return total, kwargs

result = sum_nums(4, 5, 2, 5, 6, 7, name="Peter", age=29, town="Plovdiv")
print(result)
