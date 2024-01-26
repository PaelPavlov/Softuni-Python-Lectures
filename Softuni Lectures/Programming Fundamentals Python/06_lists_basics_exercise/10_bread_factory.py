events = input().split("|")
total_energy = 100
total_coins = 100
bakery_is_open = True

for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    value_of_event = int(event_items[1])

    if type_of_event == "rest":
        initial_energy = total_energy
        total_energy += value_of_event
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")


    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += value_of_event
            print(f"You earned {value_of_event} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    

    else:
        if total_coins >= value_of_event:
            total_coins -= value_of_event
            print(f"You bought {type_of_event}")
        else:
            bakery_is_open = False
            break
if bakery_is_open:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else: #bakery_is_open = False
    print(f"Closed! Cannot afford {type_of_event}.")