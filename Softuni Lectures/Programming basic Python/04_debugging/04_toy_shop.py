# Цени на играчките:
#
# · Пъзел - 2.60 лв.
#
# · Говореща кукла - 3 лв.
#
# · Плюшено мече - 4.10 лв.
#
# · Миньон - 8.20 лв.
#
# · Камионче - 2 лв.



# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия


vacation_cost = float(input())
puzzle_count = int(input())
dolls = int(input())
teddies = int(input())
minions = int(input())
trucks = int(input())

toys_total = puzzle_count + dolls + teddies + minions + trucks
total_price = puzzle_count * 2.60 + dolls * 3 + teddies * 4.10 + minions * 8.20 + trucks * 2


if toys_total >= 50:
    total_price = total_price * (1 - 0.25) # total_price *=

total_price = total_price * (1 - 0.10)

if total_price >= vacation_cost:
    print(f"Yes! {total_price - vacation_cost:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_cost - total_price:.2f} lv needed. ")


