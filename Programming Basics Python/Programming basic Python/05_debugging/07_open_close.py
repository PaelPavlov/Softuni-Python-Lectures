time = int(input())
day_of_the_week = input()
if day_of_the_week == "Sunday" or not 10 <= time <= 18:
    print("closed")
else:
    print('open')
