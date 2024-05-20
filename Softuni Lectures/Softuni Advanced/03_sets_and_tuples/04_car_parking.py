n = int(input())
parking = set()

for _ in range(n):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking.add(car_number)
    elif direction == "OUT":
        if car_number in parking:
            parking.remove(car_number)

if parking:
    print(*parking, sep='\n')
else:
    print("Parking Lot is Empty")