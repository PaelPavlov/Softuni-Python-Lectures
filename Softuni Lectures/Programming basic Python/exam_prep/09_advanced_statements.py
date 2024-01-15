# ⦁	Билети за мач
# Когато пуснали билетите за Евро 2016, група запалянковци решили да си закупят. Билетите имат две категории с различни цени:
# ⦁	VIP – 499.99 лева.
# ⦁	Normal – 249.99 лева.
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспоОт 1 до 4 – 75% от бюджета.
# ⦁	От 5 до 9 – 60% от бюджета.
# ⦁	От 10 до 24 – 50% от бюджета.
# ⦁	От 25 до 49 – 40% от бюджета.
# ⦁	50 или повече – 25% от бюджета.

budget = float(input())
ticket_category = input()
number_of_people = int(input())
ticket_price = 0
transport_fee = 0

if ticket_category == "VIP":
    ticket_price = 499.99
    if number_of_people >= 1 and number_of_people <= 4:
        transport_fee = budget * 0.75
    elif number_of_people >= 5 and number_of_people <= 9:
        transport_fee = budget * 0.60
    elif number_of_people >= 10 and number_of_people <= 24:
        transport_fee = budget * 0.50
    elif number_of_people >= 25 and number_of_people <= 49:
        transport_fee = budget * 0.40
    else:
        transport_fee = budget * 0.25

if ticket_category == "Normal":
    ticket_price = 249.99
    if number_of_people >= 1 and number_of_people <= 4:
        transport_fee = budget * 0.75
    elif number_of_people >= 5 and number_of_people <= 9:
        transport_fee = budget * 0.60
    elif number_of_people >= 10 and number_of_people <= 24:
        transport_fee = budget * 0.50
    elif number_of_people >= 25 and number_of_people <= 49:
        transport_fee = budget * 0.40
    else:
        transport_fee = budget * 0.25
# tickets_total = number_of_people * ticket_price
# expense = tickets_total + transport_fee
summary = (number_of_people * ticket_price) + transport_fee



if summary < budget:
    total_cost = budget - summary
    print(f"Yes! You have {total_cost:.2f} leva left.")
else:
    total_cost = summary - budget
    print(f"Not enough money! You need {total_cost:.2f} leva.")

# Входът се чете от конзолата и съдържа точно 3 реда:
# ⦁	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# ⦁	На втория ред е категорията – "VIP" или "Normal"
# ⦁	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]


#
# Изход
# Да се отпечата на конзолата един ред:
# ⦁	Ако бюджетът е достатъчен:
# ⦁	"Yes! You have {останалите пари на групата} leva left."
# ⦁	Ако бюджетът НЕ Е достатъчен:
# ⦁	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
