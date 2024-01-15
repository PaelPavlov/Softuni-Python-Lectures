# Задача 5. Еверест
# Атанас е алпинист, чиято следваща цел е изкачването на Еверест.
# Вашата задача е да напишете програма която да следи до каква височина е достигнал Атанас и за колко дни е изкачил върха.
# Той започва изкачването си от ден първи от базов лагер, който е на 5 364 метра, а самият връх е на 8 848м.
# Преди всяко изкачване на определени метри,
# Атанас може да си почине в някой лагер и да продължи на следващия ден или да продължи изкачването без да спре,
# като максималното време, в което той може да изкачва върха е 5 дни. Програмата приключва при получаване на командата "END",
# при достигане на върха(8 848м) или при превишаване на разрешените 5 дни за изкачване.

total_meters = 5364
days = 1
is_achieved = False
while days <= 5:
    will_rest = input().lower()

    if will_rest == "end":
        is_achieved = False
        break

    if will_rest == "yes":
        meters_climbed = int(input())
        days += 1
    else:
        meters_climbed = int(input())

    if days > 5:
        is_achieved = False
        break

    total_meters += meters_climbed if will_rest else meters_climbed

    if total_meters >= 8848:
        is_achieved = True
        break


if is_achieved:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed!\n{total_meters}")
# Вход
# От конзолата се четат по два реда до въвеждане на команда "END", ако са минали повече от 5 дни в изкачване или се достигне върха (8 848м):
# "Yes" / "No" - текст - дали Атанас ще нощува преди изкачването на следващите метри или не
# Изкачени метри - цяло число в интервала [1...4000]



# Изход
# След получаване на командата "END", превишаване на разрешениете 5 дни за изкачване или се достигне върха (8 848м), на конзолата се отпечатва:
# Ако Атанас е изкачил Еверест:
# "Goal reached for {брой дни които Атанас е изкачвал върха} days!"
# Ако Атанас НЕ е изкачил Еверест:
# "Failed!"
# "{достигнатите от Атанас метри}"


# height = 5364
# days_passed = 0
# camp_break = input()
# is_achieved = False
# while camp_break != "END" or days_passed > 5:
#     newly_climbed_height = input()
#     height += int(newly_climbed_height)
#     days_passed += 1
#     if height >= 8848:
#         is_achieved = True
#         break
#     camp_break = input()
#
# if is_achieved:
#     print(f"Goal reached for {days_passed} days!")
# else:
#     print(f"Failed! \n{height}")



# height = 5364
# days_passed = 0
# camp_break = input()
# is_achieved = False
# while camp_break != "END" or days_passed > 5:
#     if height >= 8848:
#         is_achieved = True
#         break
#     newly_climbed_height = input()
#     if newly_climbed_height == "Yes":
#         days_passed += 1
#         continue
#     else:
#         height += int(newly_climbed_height)
#         days_passed += 1
#
#     camp_break = input()
#
# if is_achieved:
#     print(f"Goal reached for {days_passed} days!")
# else:
#     print(f"Failed! \n {height}")