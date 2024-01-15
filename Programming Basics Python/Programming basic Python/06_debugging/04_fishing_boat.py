budget = int(input())
season = input()
fishermen = int(input())

boat_rent = 0
discount = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishermen <= 6:
    discount = 0.10
elif fishermen <= 11:
    discount = 0.15
else:
    discount = 0.25

extra_discount = 0

if fishermen % 2 == 0 and season != "Autumn":         # % 2 == 0 proverka ako chisloto e chetno
    extra_discount = 0.05

total_cost = boat_rent * (1 - discount) * (1 - extra_discount)

if budget >= total_cost:
    print(f"Yes! You have {budget - total_cost} leva left.")
else:
    print(f"Not enough money! You need {total_cost - budget} leva.")