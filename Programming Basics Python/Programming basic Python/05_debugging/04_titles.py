ages = float(input())
gender = input()
if gender == "m" and ages >= 16:
    print("Mr.")
elif gender == 'm' and ages < 16:
    print('Master')
elif gender == "f" and ages >= 16:
    print("Ms.")
elif gender == 'f' and ages < 16:
    print("Miss")