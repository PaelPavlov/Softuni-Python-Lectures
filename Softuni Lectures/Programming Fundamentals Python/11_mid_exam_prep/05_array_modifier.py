# def swap(num1, num2):
#     index1, index2 = num1, num2
#     array_as_integer[index1], array_as_integer[index2] = array_as_integer[index2], array_as_integer[index1]


# print()


def modify_array(elements):
    while True:
        command = input()
        if command == "end":
            break

        tokens = command.split()

        if tokens[0] == "swap":
            index1, index2 = map(int, tokens[1:])
            elements[index1], elements[index2] = elements[index2], elements[index1]
        elif tokens[0] == "multiply":
            index1, index2 = map(int, tokens[1:])
            elements[index1] *= elements[index2]
        elif tokens[0] == "decrease":
            elements = [element - 1 for element in elements]

    return elements


initial_array = list(map(int, input().split()))
result_array = modify_array(initial_array)
# print(", ".join(map(str, result_array)))
print(*result_array, sep=", ")