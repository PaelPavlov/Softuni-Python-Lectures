# Предлагат се и следните отстъпки:
# ⦁	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# ⦁	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# ⦁	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# ⦁	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

month = input()
nights = int(input())
price_apt = 0
price_studio = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if nights > 7 and nights < 14:
        price_studio = (studio * nights) * 0.95
        price_apt = nights * apartment
    elif nights > 14:
        price_apt = nights * (apartment * 0.90)
        price_studio = nights * (studio * 0.70)
    else:
        price_apt = nights * apartment
        price_studio = nights * studio
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        price_apt = nights * (apartment * 0.90)
        price_studio = nights * (studio * 0.80)
    else:
        price_apt = nights * apartment
        price_studio = nights * studio
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights > 14:
        price_apt = nights * (apartment * 0.90)
        price_studio = nights * studio
    else:
        price_apt = nights * apartment
        price_studio = nights * studio



print(f"Apartment: {price_apt:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# ⦁	На първия ред е месецът - May, June, July, August, September или October;
# ⦁	На втория ред е броят на нощувките - цяло число.
# Изход
# Да се отпечатат на конзолата 2 реда:
# ⦁	На първия ред: "Apartment: {цена за целият престой} lv."
# ⦁	На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.
