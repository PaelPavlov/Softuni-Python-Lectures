# Ако топката е “red” точките ни се повишават с 5.
# Ако топката е “orange” точките ни се повишават с 10.
# Ако топката е “yellow” точките ни се повишават с 15.
# Ако топката е “white” точките ни се повишават с 20.
# Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.

# Вход:
# От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
# След това се четат N на брой цветове.

balls = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
different_balls = 0
for _ in range(balls):
    color = input()
    if color == "red":
        red_balls += 1
        points += 5
    elif color == "orange":
        orange_balls += 1
        points += 10
    elif color == "yellow":
        yellow_balls += 1
        points += 15
    elif color == "white":
        white_balls += 1
        points += 20
    elif color == "black":
        black_balls += 1
        points /= 2
    else:
        different_balls += 1
        continue


print(f"Total points: {int(points)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {different_balls}")
print(f"Divides from black balls: {black_balls}")




# Изход:
# Отпечатват се следните редове:
# "Total points: {всичките събрани точки}"
# "Red balls: {броят червени топки}"
# "Orange balls: {броят оранжеви топки}"
# "Yellow balls: {броят жълти топки}"
# "White balls: {броят бели топки}"
# "Other colors picked: {броят на избраните топки извън зададените цветове}"
# "Divides from black balls: {броят на пътите, в които точките са били разделяни на 2}"
