def create_car(name, mileage, fuel):
    return {'name': name, 'mileage': mileage, 'fuel': fuel}

def refuel(car, added_fuel):
    max_fuel = 75
    fuel_to_add = min(added_fuel, max_fuel - car['fuel'])
    car['fuel'] += fuel_to_add
    print(f'{car["name"]} refueled with {fuel_to_add} liters')

def drive(car, distance, required_fuel):
    if car['fuel'] >= required_fuel:
        car['mileage'] += distance
        car['fuel'] -= required_fuel
        print(f'{car["name"]} drive for {distance} kilometers. {required_fuel} liters of fuel consumed.')
        if car['mileage'] >= 100000:
            print(f"Tme to sell the {car['name']}!")
            return True
    else:
        print("Not enough fuel to make thar ride")

def revert(car, kilometers):
    car['mileage'] -= kilometers
    if car['mileage'] < 10000:
        car['mileage'] = 10000
    else:
        print(f'{car["name"]} mileage decreased by {kilometers} kilometers')

def main_function():
    n = int(input())
    cars = []

    for _ in range(n):
        car_info = input().split('|')
        car = create_car(car_info[0], int(car_info[1]), int(car_info[2]))
        cars.append(car)

    while True:
        command = input()

        if command == 'Stop':
            break
        tokens = command.split(':')
        action = tokens[0]
        car_name = tokens[1]

        for car in cars:
            if car['name'] == car_name:
                if action == "Drive":
                    distance = int(tokens[2])
                    fuel = int(tokens[3])
                    if drive(car, distance, fuel):
                        cars.remove(car)

                elif action == "Refuel":
                    added_fuel = int(tokens[2])
                    refuel(car, added_fuel)
                
                elif action == "Revert":
                    kilometers = int(tokens[2])
                    revert(car, kilometers)
    for car in cars:
        print(f"{car['name']} -> Mileage: {car['mileage']} kms, Fuel in the tank: {car['fuel']} lt.")

main_function()