# Напишете програма която пресмята колко пари ще изкара шофьор на ТИР за един сезон.
# На входа програмата получава през кой сезон ще работи шофьора, както и колко километра на месец ще кара.
# Един сезон е 4 месеца. Според зависи сезона и броя километри на месец ще му се заплаща различна сума на километър:


season = input()
kms_per_month = float(input())
price_per_km = 0

if season == "Summer":
    if kms_per_month <= 5000:
        price_per_km = 0.90
    elif kms_per_month > 5000 and kms_per_month <= 10000:
        price_per_km = 1.10
    elif kms_per_month > 10000 and kms_per_month <= 20000:
        price_per_km = 1.45

if season == "Winter":
    if kms_per_month <= 5000:
        price_per_km = 1.05
    elif kms_per_month > 5000 and kms_per_month <= 10000:
        price_per_km = 1.25
    elif kms_per_month > 10000 and kms_per_month <= 20000:
        price_per_km = 1.45

if season == "Autumn" or season == "Spring":
    if kms_per_month <= 5000:
        price_per_km = 0.75
    elif kms_per_month > 5000 and kms_per_month <= 10000:
        price_per_km = 0.95
    elif kms_per_month > 10000 and kms_per_month <= 20000:
        price_per_km = 1.45

earnings = kms_per_month * price_per_km
seasonal_earnings = (earnings * 4) * 0.90 #taxed

print(f"{seasonal_earnings:.2f}")
# Вход
# Входът се чете от конзолата и се състои от два реда:
# ⦁	Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
# ⦁	Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]

#
# Изход
# На конзолата трябва да се отпечатат едно число:
# ⦁	Заплатата на шофьора след данъците, форматирана до втория знак след десетичната запетая.
