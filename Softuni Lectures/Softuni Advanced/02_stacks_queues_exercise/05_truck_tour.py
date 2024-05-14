from collections import deque


pumps_num = int(input())
pumps = deque()


for _ in range(pumps_num):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

start_position = 0
stops = 0

while stops < pumps_num:
    fuel = 0
    for i in range(pumps_num):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)