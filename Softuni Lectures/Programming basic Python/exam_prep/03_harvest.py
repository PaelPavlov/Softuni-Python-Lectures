# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.
import math


square_meters = int(input())
grapes_for_square_meter = float(input())
needed_liters_wine = int(input())
needed_workers = int(input())
one_liter_of_wine = 2.5

potential_grapes_produced = (square_meters * grapes_for_square_meter) * 0.40 / one_liter_of_wine

if potential_grapes_produced < needed_liters_wine:
    leftover_wine = needed_liters_wine - potential_grapes_produced
    print(f"It will be a tough winter! More {math.floor(leftover_wine)} liters wine needed.")
else:
    leftover_wine = potential_grapes_produced - needed_liters_wine
    given_wine = leftover_wine / needed_workers
    print(f"Good harvest this year! Total wine: {math.floor(potential_grapes_produced)} liters.")
    print(f"{math.floor(leftover_wine)} liters left -> {math.ceil(given_wine)} liters per person.")



#
# Изход
# На конзолата трябва да се отпечата следното:
# Ако произведеното вино е по-малко от нужното:
# “It will be a tough winter! More {недостигащо вино} liters wine needed.”
# Резултатът трябва да е закръглен към по-ниско цяло число
# Ако произведеното вино е колкото или повече от нужното:
# “Good harvest this year! Total wine: {общо вино} liters.”
# Резултатът трябва да е закръглен към по-ниско цяло число
# “{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# И двата резултата трябва да са закръглени към по-високото цяло число
