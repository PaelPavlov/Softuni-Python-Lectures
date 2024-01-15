town = input()
sales = float(input())
coms = 0

if town == "Sofia" and sales > 0:
    if sales > 0 and sales <= 500:
        coms = 0.05
    elif sales > 500 and sales <= 1000:
        coms = 0.07
    elif sales > 1000 and sales <= 10000:
        coms = 0.08
    elif sales > 10000:
        coms = 0.12
    print(f"{sales * coms:.2f}")

elif town == "Varna" and sales > 0:
    if sales > 0 and sales <= 500:
        coms = 0.045
    elif sales > 500 and sales <= 1000:
        coms = 0.075
    elif sales > 1000 and sales <= 10000:
        coms = 0.10
    elif sales > 10000:
        coms = 0.13
    print(f"{sales * coms:.2f}")

elif town == "Plovdiv" and sales > 0:
    if sales > 0 and sales <= 500:
        coms = 0.055
    elif sales > 500 and sales <= 1000:
        coms = 0.08
    elif sales > 1000 and sales <= 10000:
        coms = 0.12
    elif sales > 10000:
        coms = 0.145
    print(f"{sales * coms:.2f}")

else:
    print("error")

