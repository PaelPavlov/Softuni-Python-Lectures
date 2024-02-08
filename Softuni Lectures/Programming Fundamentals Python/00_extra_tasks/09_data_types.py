
def int_multiply(value):
    return 2 * int(value)

def real_multiply(value):
    return "{:.2f}".format(float(value) * 1.5)

def string_format(value):
    return "$" + value + "$"

def menu(command, value):   
    if command == "int":
        return int_multiply(value)
    elif command == "real":
        return real_multiply(value)
    else:
        return string_format(value)


command = input()
value = input()

result = menu(command, value)
print(result)
