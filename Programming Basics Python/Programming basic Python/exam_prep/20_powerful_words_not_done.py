import sys

command = input()
max_points = -sys.maxsize
command_max = ""
points = 0

while command != "End of words":
    for char in command:
        current_points = 0
        if str(command[0]) == "A" or str(command[0]) == "E" or str(command[0]) == "I" or str(command[0]) == "O" or str(
                command[0]) == "U" or str(command[0]) == "Y":
            current_points += (ord(char) * len(command))
        else:
            current_points += (ord(char) / len(command))


        if current_points > max_points:
            max_points = current_points
            command_max = command

    command = input()
print(f"The most powerful word is {command_max} - {round(max_points)}")

