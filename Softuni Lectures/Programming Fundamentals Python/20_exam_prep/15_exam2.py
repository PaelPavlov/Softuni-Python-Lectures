message = input()

while True:
    command = input().split()

    if command[0] == "Finish":
        break

    elif command[0] == "Replace":
        string, substring = command[1], command[2]
        message = message.replace(string, substring)
        print(message)

    elif command[0] == "Cut":
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            message = message[:start_index] + message[end_index+1:]
            print(message)
        else:
            print("Invalid indices!")

    elif command[0] == "Make":
        upper_lower = command[1]
        if upper_lower == "Upper":
            message = message.upper()
        elif upper_lower == "Lower":
            message = message.lower()
        print(message)

    elif command[0] == "Check":
        substring = command[1]
        if substring in message:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif command[0] == "Sum":
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            substring = message[start_index:end_index+1]
            sum_of_chars = sum(ord(char) for char in substring)
            print(sum_of_chars)
        else:
            print("Invalid indices!")