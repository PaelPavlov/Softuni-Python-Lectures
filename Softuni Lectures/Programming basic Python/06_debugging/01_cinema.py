# ⦁	Кино
# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
# ⦁	Premiere - премиерна прожекция, на цена 12.00 лева;
# ⦁	Normal - стандартна прожекция, на цена 7.50 лева;
# ⦁	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00
#
#
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
# въведени от потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2
# знака след десетичната точка.


premiere = 12.00
normal = 7.50
discount = 5.00

screening = input()
rows = int(input())
columns = int(input())

income = 0

capacity = rows * columns
if screening == "Premiere":
    income = capacity * 12.00
elif screening == "Normal":
    income = capacity * 7.50
elif screening == "Discount":
    income = capacity * 5.00

print(f"{income:.2f} leva")