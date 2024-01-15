# Иванчо е на 18 години и получава наследство, което се състои от X сума пари и машина на времето.
# Той решава да се върне до 1800 година, но не знае дали парите ще са достатъчни, за да живее без да работи.
# Напишете програма, която пресмята, дали Иванчо ще има достатъчно пари, за да не се налага да работи до дадена година включително.
# Като приемем, че за всяка четна (1800, 1802 и т.н.) година ще харчи 12 000 лева.
# За всяка нечетна (1801,1803  и т.н.) ще харчи 12 000 + 50 * [годините, които е навършил през дадената година].

nasledstvo = float(input())
year_to_live_to = int(input())
year = 1799
years = 18
expense = 0

for _ in range(year, year_to_live_to):
    if year >= 1800:
        years += 1
    year += 1
    if year % 2 == 0:
        expense += 12000
    else:
        expense += 12000 + (years * 50)


if expense <= nasledstvo:
    money_left_with = nasledstvo - expense
    print(f"Yes! He will live a carefree life and will have {money_left_with:.2f} dollars left.")
else:
    money_needed = expense - nasledstvo
    print(f"He will need {money_needed:.2f} dollars to survive.")



# Изход
# Да се отпечата на конзолата 1 ред. Сумата трябва да е форматирана до два знака след десетичната запетая:
# Ако парите са достатъчно:
# "Yes! He will live a carefree life and will have {N} dollars left." – където N са парите, които ще му останат.
# Ако парите НЕ са достатъчно:
# "He will need {М} dollars to survive." – където M е сумата, която НЕ достига.
