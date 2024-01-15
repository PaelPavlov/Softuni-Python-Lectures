# Ако числото е до 100 включително, бонус точките са 5;
#
# · Ако числото е по-голямо от 100, бонус точките са 20% от числото;
#
# · Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
#
# · Допълнителни бонус точки (начисляват се отделно от предходните):
#
# o За четно число à + 1 т.
#
# o За число, което завършва на 5 à + 2 т.

starting_points = int(input())

bonus_points = 0
if starting_points <= 100:
    bonus_points = 5
elif 1000 >= starting_points > 100:
    bonus_points = 0.20 * starting_points
else:
    bonus_points = 0.10 * starting_points

if starting_points % 2 == 0: #boolean check for even numbers
    bonus_points = bonus_points + 1
if starting_points % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(starting_points + bonus_points)