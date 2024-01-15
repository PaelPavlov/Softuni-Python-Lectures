# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).
# ⦁	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# ⦁	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# ⦁	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# ⦁	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
import math

shape = input()

if shape == "square":
    length = float(input())
    print(f"{length * length :.3f}")
elif shape == "rectangle":
    length = float(input())
    width = float(input())
    print(f"{length * width :.3f}")
elif shape == "circle":
    length = float(input())
    print(f"{math.pi * length * length :.3f}")
elif shape == "triangle":
    length1 = float(input())
    length2 = float(input())
    print(f"{length1 * length2 * 0.5 :. 3f}")
