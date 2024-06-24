from collections import deque

total_kills = 0
monster_armors = deque([int(el) for el in input().split(",")])
soldier_strikes = [int(el) for el in input().split(",")]

while monster_armors and soldier_strikes:
    current_monster_defence = monster_armors.popleft()
    current_soldier_power = soldier_strikes.pop()

    if current_soldier_power >= current_monster_defence:
        total_kills += 1
        current_soldier_power -= current_monster_defence
        if not soldier_strikes and current_soldier_power > 0:
            soldier_strikes.append(current_soldier_power)
        elif soldier_strikes:
            soldier_strikes[-1] += current_soldier_power
    else:
        current_monster_defence -= current_soldier_power
        monster_armors.append(current_monster_defence)

if not monster_armors:
    print(f"All monsters have been killed!")
if not soldier_strikes:
    print(f"The soldier has been defeated.")
print(f"Total monsters killed: {total_kills}")