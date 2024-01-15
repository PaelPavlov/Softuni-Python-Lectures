# Вие сте режисьор на филма "Програмирането е забавно", като имате определено време за снимки. От вас се
# иска да напишете програма, с която ще разберете дали снимачният ден ще ви стигне да заснемете филма.
# Снимачният ден започва с подготовка на терен, което е 15 процента от времето за снимки! Филмът има
# определен брой сцени, които се заснемат за определено време.



shooting_length = int(input())
scenes = int(input())
scene_length = int(input())

preparations = shooting_length * 0.15
needed_time = scenes * scene_length + preparations


if needed_time < shooting_length:
    print(f"You managed to finish the movie on time! You have {round(shooting_length - needed_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(needed_time - shooting_length)} minutes.")




# Изход
# На конзолата да се отпечата един ред:
#  Ако времето за заснемане на филма ви стигне:
# "You managed to finish the movie on time! You have {останало време} minutes left!"
#  Ако времето НЕ ВИ стигне:
# "Time is up! To complete the movie you need {нужно време} minutes."