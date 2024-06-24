ROWS_COUNT, COL_COUNT = [int(el) for el in input().split(",")]


def is_in_area(row, col):
    return 0 <= row < ROWS_COUNT and 0 <= col < COL_COUNT



matrix = []
total_cheese_count = 0
eaten_cheese_count = 0
mouse_position = None

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for row_index in range(ROWS_COUNT):
    row_data = list(input())
    if "M" in row_data:
        col_index = row_data.index("M")
        mouse_position = [row_index, col_index]
    total_cheese_count += row_data.count("C")
    matrix.append(row_data)

direction = input()

while direction != "danger":
    current_row, current_col = mouse_position
    row_to_go, col_to_go = direction_mapper[direction]
    desired_row = current_row + row_to_go
    desired_col = current_col + col_to_go

    if not is_in_area(desired_row, desired_col):
        print("No more cheese for tonight!")
        break

    elif matrix[desired_row][desired_col] == "C":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        eaten_cheese_count += 1
        mouse_position = [desired_row, desired_col]

        if eaten_cheese_count == total_cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[desired_row][desired_col] == "T":
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        print("Mouse is trapped!")
        break

    elif matrix[desired_row][desired_col] == "@":
        direction = input()
        continue

    else:
        matrix[desired_row][desired_col] = "M"
        matrix[current_row][current_col] = "*"
        mouse_position = [desired_row, desired_col]

    direction = input()

if direction == "danger":
    print("Mouse will come back later!")

for row in matrix:
    print(*row, sep="")
