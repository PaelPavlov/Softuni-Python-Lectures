
targets = input().split(" ")
targets = list(map(int, targets))

line = input()

while line != "End":
    command_list = line.split(" ")
    command = command_list[0]
    index = int(command_list[1])
    value = int(command_list[2])

    if command == "Shoot" and index >= 0 and index < len(targets):
        current_target = targets[index]
        current_target -= value
        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target
    elif command == "Add":
        if index >= 0 and index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    line = input()

targets = list(map(str, targets))
output = "|".join(targets)
print(output)
