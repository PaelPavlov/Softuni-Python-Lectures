# # На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри, разстоянието в метри,
# # което трябва да преплува и времето в секунди, за което плува разстояние от 1 м.
# Да се напише програма, която изчислява дали се е справил със задачата, като се има предвид, че:
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява колко пъти
# Иван ще се забави, в резултат на съпротивлението на водата, резултатът
# трябва да се закръгли надолу до най-близкото цяло число.
# #
import math

record_seconds = float(input())
length_meters = float(input())
time_swimming_seconds_one_meter = float(input())

time_needed = length_meters * time_swimming_seconds_one_meter
slowdown = math.floor(length_meters / 15) * 12.5
slowed_down_time = time_needed + slowdown

if slowed_down_time < record_seconds:
    print(f" Yes, he succeeded! The new world record is {slowed_down_time:.2f} seconds.")
else:
    result = slowed_down_time - record_seconds
    print(f'No, he failed! He was {result:.2f} seconds slower.')
