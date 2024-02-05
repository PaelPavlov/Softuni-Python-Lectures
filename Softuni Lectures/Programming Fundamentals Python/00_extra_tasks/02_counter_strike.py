initial_energy = int(input())
battles_won = 0
fighting = True

while fighting:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
        fighting = False
        break


    if initial_energy >= int(distance):
        initial_energy -= int(distance)
        battles_won += 1
        if battles_won % 3 == 0:
            initial_energy += battles_won
       
    
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        fighting = False
        break
