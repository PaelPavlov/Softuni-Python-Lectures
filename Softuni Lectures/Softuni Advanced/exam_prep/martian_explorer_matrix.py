SIZE = 6

deposits = {"W": ["Water", 0], "M": ["Metal", 0], "C": ["Concrete", 0]}

#### Mirror movement across matrix using lambda functions

directions = {
    "up": lambda r, c: [(r - 1), c % SIZE],
    "down": lambda r, c: [(r + 1), c % SIZE],
    "right": lambda r, c: [r, (c + 1) % SIZE],
    "left": lambda r, c: [r, (c - 1) % SIZE]
}

mars = []
rover_pos = []

for row in range(SIZE):
    current_row = input().split()

    if "E" in current_row:
        rover_pos = [row, current_row.index("E")]
    mars.append(current_row)

commands = input().split(", ")

for command in commands:
    rover_pos = directions[command](*rover_pos) #We unpack the rover pos because we send the args to the lamba function
                                                # in the directions mapper
    position = mars[rover_pos[0]][rover_pos[1]]

    if position in deposits:
        print(f"{deposits[position][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")

        deposits[position][1] += 1

    elif position == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if all([deposits["W"][1], deposits["M"][1], deposits["C"][1]]):
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")