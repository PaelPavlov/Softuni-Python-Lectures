fruit = input()
day_of_the_week = input()
quantity = float(input())
fruit_price = 0
if day_of_the_week == "Monday" \
        or day_of_the_week == "Tuesday" \
        or day_of_the_week == "Wednesday" \
        or day_of_the_week == "Thursday" \
        or day_of_the_week == "Friday":
    if fruit == "banana":
        fruit_price = 2.50
    elif fruit == "apple":
        fruit_price = 1.20
    elif fruit == "orange":
        fruit_price = 0.85
    elif fruit == "grapefruit":
        fruit_price = 1.45
    elif fruit == "kiwi":
        fruit_price = 2.70
    elif fruit == "pineapple":
        fruit_price = 5.50
    elif fruit == "grapes":
        fruit_price = 3.85

elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if fruit == "banana":
        fruit_price = 2.70
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.90
    elif fruit == "grapefruit":
        fruit_price = 1.60
    elif fruit == "kiwi":
        fruit_price = 3.00
    elif fruit == "pineapple":
        fruit_price = 5.60
    elif fruit == "grapes":
        fruit_price = 4.20

if fruit_price == 0:
    print("error")
else:
    fruit_price *= quantity
    print(f"{fruit_price:.2f}")
