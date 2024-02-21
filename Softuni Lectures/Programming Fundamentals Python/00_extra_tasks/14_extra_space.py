# travel_route = input().split("||")
# fuel = int(input())
# ammunition = int(input())

# commands = []
# travelling = True

# while travelling:
#     commands = travel_route.split(", ")
#     command = commands[0]
#     amount = commands[1]

#     if command[0] == 'Travel':
#         if fuel > command[1]:
#             fuel -= command[1]
#             print(f"The spaceship travelled {command[1]} light-years.")
#         else:
#             print("Mission failed.")
#             travelling = False
#             break
#     elif command[0] == 'Enemy':
#         if ammunition > command[1]:
#             ammunition -= command[1]
#             print(f"An enemy with {command[1]} armour is defeated.")
#         elif ammunition < command[1]:
#             if fuel * 2 > command[1]:
#                 fuel = command[1] * 2
#                 print(f"An enemy with {command[1]} armour is outmaneuvered.")
#             else:
#                 print("Mission failed.")
#                 travelling = False
#                 break
#     elif command[0] == 'Repair':
#         fuel += command[1]
#         added_fuel = fuel + command[1]
#         ammunition += command[1] * 2
#         added_ammo = ammunition + (command[1]) * 2
#         print(f"Ammunitions added: {added_ammo}.")
#         print(f"Fuel added: {added_fuel}.")
#     elif command[0] == 'Titan':
#         print("You have reached Titan, all passengers are safe.")
#         travelling = False
#         break

travel_route = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())

current_fuel = starting_fuel
current_ammunition = starting_ammunition


for command in travel_route:
    commands = command.split()
    action = commands[0]
    
    if action == "Travel":
        distance = int(commands[1])
        if current_fuel >= distance:
            print(f"The spaceship travelled {distance} light-years.")
            current_fuel -= distance
        else:
            print("Mission failed.")
            break
    
    elif action == "Enemy":
        armor = int(commands[1])
        if current_ammunition >= armor:
            print(f"An enemy with {armor} armour is defeated.")
            current_ammunition -= armor
        elif current_fuel >= armor * 2:
            print(f"An enemy with {armor} armour is outmaneuvered.")
            current_fuel -= armor * 2
        else:
            print("Mission failed.")
            break
    
    elif action == "Repair":
        ammunition_added = int(commands[1]) * 2
        fuel_added = int(commands[1])
        current_ammunition += ammunition_added
        current_fuel += fuel_added
        print(f"Ammunitions added: {ammunition_added}.")
        print(f"Fuel added: {fuel_added}.")
    
    elif action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break


# route = input().split("||")
# fuel = int(input())
# ammunition = int(input())

# mission_success = True
# for segment in route:
#     command, *args = segment.split()
#     if command == "Travel":
#         distance = int(args[0])
#         if fuel >= distance:
#             print(f"The spaceship travelled {distance} light-years.")
#             fuel -= distance
#         else:
#             mission_success = False
#             break
#     elif command == "Enemy":
#         enemy_points = int(args[0])
#         if ammunition >= enemy_points:
#             print(f"An enemy with {enemy_points} armour is defeated.")
#             ammunition -= enemy_points
#         elif fuel >= enemy_points * 2:
#             print(f"An enemy with {enemy_points} armour is outmaneuvered.")
#             fuel -= (enemy_points * 2)
#         else:
#             mission_success = False
#             break
#     elif command == "Repair":
#         added_ammunition = int(args[0])*2
#         added_fuel = int(args[0])
#         print(f"Ammunitions added: {added_ammunition}.")
#         print(f"Fuel added: {added_fuel}.")
#         ammunition += added_ammunition
#         fuel += added_fuel
#     elif command == "Titan":
#         print("You have reached Titan, all passengers are safe.")
#         mission_success = True
#         break

# if not mission_success:
#     print("Mission failed.")