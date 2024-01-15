# Дядо Коледа много обича да пътешества, но за съжаление се случило,
# така че точно преди да замине на почивка три от елените му се разболяли и трябва да ги остави.
# Когато заминава, той трябва да съобрази колко храна да остави на всеки един от елените, за да не останат гладни.
# Напишете програма, която пресмята дали оставената от Дядо Коледа храна ще е достатъчна за времето, в което него няма да го има.
# Всеки елен изяжда определено количество храна на ден.
import math



number_of_days = int(input())
food_he_left = int(input())
food_per_day_first_deer = float(input())
food_per_day_second_deer = float(input())
food_per_day_third_deer = float(input())

food_to_be_eaten = (food_per_day_third_deer + food_per_day_second_deer + food_per_day_first_deer) * number_of_days
food_left = food_he_left - food_to_be_eaten

if food_to_be_eaten <= food_he_left:
    print(f"{int(food_left)} kilos of food left.")
else:
    food_needed = food_to_be_eaten - food_he_left
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")


# Изход:
# На конзолата трябва да се отпечата на един ред:
# Ако оставената храна Е достатъчна:
# “{килограми, които остават} kilos of food left.”
# Резултатът трябва да е закръглен към ПО-МАЛКОТО цяло число
# Ако оставената храна НЕ Е достатъчна:
# “{килограми, които не  недостигат} more kilos of food are needed.”
# Резултатът трябва да е закръглен към ПО-ГОЛЯМОТО цяло число
