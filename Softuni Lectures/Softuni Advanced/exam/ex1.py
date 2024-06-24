from collections import deque

packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])

weight_delivered = 0


while packages and couriers:
    package = packages.pop()
    courier = couriers.popleft()

    if courier >= package:
        weight_delivered += package
        if courier > package:
            courier -= 2 * package
            if courier > 0:
                couriers.append(courier)
    elif courier < package:
        package -= courier
        weight_delivered += courier
        packages.append(package)




print(f"Total weight: {weight_delivered} kg")
if not packages and not couriers:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")

