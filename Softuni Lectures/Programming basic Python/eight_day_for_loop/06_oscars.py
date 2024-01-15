# ⦁	Оскари
# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса.
# Академията ще ви даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка.
# Точките, които актьора получава се формират от: дължината на името на оценяващия умножено по точките, които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор е получил номинация.

# Вход
# ⦁	Име на актьора - текст
# ⦁	Точки от академията - реално число в интервала [2.0... 450.5]
# ⦁	Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# ⦁	Име на оценяващия - текст
# ⦁	Точки от оценяващия - реално число в интервала [1.0... 50.0]
#

actor_name = input()
academy_score = float(input())
jury_number = int(input())
score_total = 0
score_total += academy_score

for _ in range(jury_number):
    jury_member = input()
    jury_score = float(input())
    jury_current_score = len(jury_member) * jury_score
    score_total += jury_current_score / 2


    if score_total >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {score_total:.1f}!")
        break

if score_total < 1250.5:
    needed_score = 1250.5 - score_total
    print(f"Sorry, {actor_name} you need {needed_score:.1f} more!")





# Изход
# Да се отпечата на конзолата един ред:
# ⦁	Ако точките са над 1250.5:
# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
# ⦁	Ако точките не са достатъчни:
# 	"Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!
