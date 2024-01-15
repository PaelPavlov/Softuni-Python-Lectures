steps = 0

is_achieved = False

while not is_achieved:
    command = input()
    if command == "Going home":
        to_home_steps = int(input())
        steps += to_home_steps
        if steps >= 10000:
            is_achieved = True
        break

    current_steps = int(command) #eg int("2000") > 2000
    steps += current_steps
    if steps >= 10000:
        is_achieved = True

if is_achieved:
    print(f"Goal reached! Good job!")
    print(f"{steps - 10000} steps over the goal!")
else:
    print(f"{10000 - steps} more steps to reach goal.")