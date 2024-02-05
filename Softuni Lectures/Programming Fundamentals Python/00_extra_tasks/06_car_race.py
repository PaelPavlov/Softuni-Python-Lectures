race = [int(cars) for cars in input().split()]
middle_of_racetrack = len(race) // 2
left_racetrack = race[:middle_of_racetrack]
right_racetrack = race[middle_of_racetrack + 1:]

total_time_left = 0
total_time_right = 0

for checkpoint in left_racetrack:
    if checkpoint != 0:
        total_time_left += checkpoint
    else:
        total_time_left = total_time_left * 0.8

for checkpoint in right_racetrack:
    if checkpoint != 0:
        total_time_right += checkpoint
    else:
        total_time_right = total_time_right * 0.8

if total_time_left < total_time_right:
    print(f"The winner is left with total time: {total_time_left:.1f}")
else:
    print(f"The winner is right with total time: {total_time_right:.1f}")

