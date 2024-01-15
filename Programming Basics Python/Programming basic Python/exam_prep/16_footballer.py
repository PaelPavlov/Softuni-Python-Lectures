import sys

goals = 0
footballer = ""
best_footballer = ""
max_goals = -sys.maxsize
player = input()

while player != "END":
    footballer = player
    goals = int(input())

    if goals > max_goals:
        max_goals = goals
        best_footballer = footballer
        if max_goals > 10:
            break

    player = input()
print(f"{best_footballer} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
