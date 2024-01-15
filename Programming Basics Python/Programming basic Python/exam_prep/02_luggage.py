above_20 = float(input())
kgs = float(input())
days_until_travel = int(input())
bags = int(input())

price = 0
checkout = 0

if kgs < 10:
    price = above_20 * 0.20
elif kgs >= 10 and kgs <= 20:
    price = above_20 * 0.50
else:
    price = above_20

if days_until_travel < 7:
    checkout = price * 1.40 * bags
elif days_until_travel >= 7 and days_until_travel <= 30:
    checkout = price * 1.15 * bags
else:
    checkout = price * 1.10 * bags

print(f" The total price of bags is: {checkout:.2f} lv. ")

