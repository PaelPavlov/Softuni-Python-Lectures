n = int(input())


matrix = []
restored = False
bee_hive_reached = False
nectar = 0
energy = 15


for row in range(n):
    matrix.append([el for el in input()])
    for col in range(n):
        if matrix[row][col] == 'B':
            bee_row, bee_col = row, col
            matrix[bee_row][bee_col] = '-'


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    energy -= 1
    if (0 <= bee_row + directions[direction][0] < n) and (0 <= bee_col + directions[direction][1] < n):
        bee_row += directions[direction][0]
        bee_col += directions[direction][1]
    else:
        if direction == 'up':
            bee_row = n - 1
        elif direction == 'down':
            bee_row = 0
        elif direction == 'left':
            bee_col = n - 1
        elif direction == 'right':
            bee_col = 0
    if matrix[bee_row][bee_col].isdigit():
        nectar += int(matrix[bee_row][bee_col])
        matrix[bee_row][bee_col] = '-'
    if matrix[bee_row][bee_col] == 'H':
        bee_hive_reached = True
        break
    if energy == 0:
        if nectar > 30 and restored is False:
            energy += nectar - 30
            nectar = 30
            restored = True
        else:
            break

matrix[bee_row][bee_col] = 'B'
if bee_hive_reached:
    if nectar >= 30:
        print(f'Great job, Beesy! The hive is full. Energy left: {energy}')
    else:
        print('Beesy did not manage to collect enough nectar.')
else:
    print('This is the end! Beesy ran out of energy.')

for row in matrix:
    print(''.join(row))
