experience_needed = float(input())
count_of_battles = int(input())
experience_gained = 0
day = 0

for battle in range(1, count_of_battles + 1):

    experience = float(input())
    day += 1
    if battle % 15 == 0:
        experience *= 1.10   
    if battle % 5 == 0:
        experience *= 0.9         
    if battle % 3 == 0:
        experience *= 1.15
    experience_gained += experience     
    if experience_gained >= experience_needed:
        break
  

if experience_gained >= experience_needed:
    print(f"Player successfully collected his needed experience for {day} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed - experience_gained:.2f} more needed.")



