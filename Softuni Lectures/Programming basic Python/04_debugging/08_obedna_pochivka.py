# От конзолата се четат 3 реда:
#
# 1. Име на сериал – текст
#
# 2. Продължителност на епизод – цяло число в диапазона [10… 90]
#
# 3. Продължителност на почивката – цяло число в диапазона [10… 120]
import math

# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма, с
# която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и
# време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.

series = input()
series_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
relax_time = break_length / 4

time_left = break_length - lunch_time - relax_time

# · Ако времето е достатъчно да изгледате епизода:
#
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."

if time_left >= series_length:
    time1 = math.ceil(time_left - series_length)
    print(f"You have enough time to watch {series} and left with {time1} minutes free time.")
else:
    time2 = math.ceil(series_length - time_left)
    print(f"You don't have enough time to watch {series}, you need {time2} more minutes.")

#  Ако времето не Ви е достатъчно:
#
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."