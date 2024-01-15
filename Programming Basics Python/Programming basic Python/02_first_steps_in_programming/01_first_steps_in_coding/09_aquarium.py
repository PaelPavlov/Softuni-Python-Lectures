


length = int(input())
width = int(input())
height = int(input())
occupied_space = float(input()) / 100

total_size = length * width * height #cm * cm * cm
total_size_liters = total_size / 1000 #v decimetri dm
liters_needed = total_size_liters * (1 - occupied_space)


print(liters_needed)