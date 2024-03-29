# Млад програмист разполага с определен бюджет и свободно време в даден сезон. Напишете програма,
# която да приема на входа бюджета и сезона, а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг,
# а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел. Всеки къмпинг или хотел, според дестинацията,
# има собствена цена, която отговаря на даден процент от бюджета:
#
#
# ⦁	При 100 лв. или по-малко - някъде в България:
# ⦁	Лято - 30% от бюджета;
# ⦁	Зима - 70% от бюджета.
# ⦁	При 1000 лв. или по малко - някъде на Балканите:
# ⦁	Лято - 40% от бюджета;
# ⦁	Зима - 80% от бюджета.
# ⦁	При повече от 1000 лв. - някъде из Европа:
# ⦁	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
#

budget = float(input())
season = input()  # summer or winter

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        print(f"Camp - {budget * 0.30:.2f}")
    elif season == "winter":
        print(f"Hotel - {budget * 0.70:.2f}")

if budget <= 1000 and budget > 100:
    print("Somewhere in Balkans")
    if season == "summer":
        print(f"Camp - {budget * 0.40:.2f}")
    elif season == "winter":
        print(f"Hotel - {budget * 0.80:.2f}")

if budget > 1000:
    print("Somewhere in Europe")
    if season == "summer":
        print(f"Hotel - {budget * 0.90:.2f}")
    elif season == "winter":
        print(f"Hotel - {budget * 0.90:.2f}")

