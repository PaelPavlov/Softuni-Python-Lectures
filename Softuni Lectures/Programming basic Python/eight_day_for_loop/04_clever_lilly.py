age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
total_toys = 0
for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        current_money = birthday * 5 ### birthday * 10 / 2
        total_money += current_money
        total_money -= 1 #brother takes money
    else:
        total_toys += 1


toys_money = total_toys * toy_price
total_money += toys_money

if total_money >= washing_machine_price:
    rest_money = total_money - washing_machine_price
    print(f"Yes! {rest_money:.2f}")
else:
    needed_money = washing_machine_price - total_money
    print(f"No! {needed_money:.2f}")