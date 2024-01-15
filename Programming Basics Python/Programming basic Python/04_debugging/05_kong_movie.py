budget = float(input())
actors = int(input())
costumes = float(input())

decor = budget * 0.10
if actors > 150:
    costumes = costumes * 0.90

needed_money = decor + actors * costumes

if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {needed_money - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - needed_money:.2f} leva left.")

