climbers_groups_count = int(input())
mussala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_count = 0


for _ in range(climbers_groups_count):
    climbers_members = int(input())
    total_count += climbers_members

    if climbers_members <= 5:
        mussala_count += climbers_members
    elif climbers_members <= 12:
        montblanc_count += climbers_members
    elif climbers_members <= 25:
        kilimanjaro_count += climbers_members
    elif climbers_members <= 40:
        k2_count += climbers_members
    else:
        everest_count += climbers_members

musala_percent = mussala_count / total_count * 100
montblanc_percent = montblanc_count / total_count * 100
kilimanjaro_percent = kilimanjaro_count / total_count * 100
k2_percent = k2_count / total_count * 100
everest_percent = everest_count / total_count * 100

print(f"{musala_percent:.2f}%")
print(f"{montblanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
