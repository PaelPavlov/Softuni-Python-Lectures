p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

numbers_count = int(input())

for _ in range(numbers_count):
    current_number = int(input())
    if current_number < 200:
        p1_count += 1
    elif current_number < 400:
        p2_count += 1
    elif current_number < 600:
        p3_count += 1
    elif current_number < 800:
        p4_count += 1
    else:
        p5_count += 1

# percent = target / total * 100
# total_count = p1_count + p2_count + p3_count + p4_count + p5_count

p1_percent = p1_count / numbers_count * 100 # 0.6666666 => 66.66666666 => 66.67
p2_percent = p2_count / numbers_count * 100 # 0.6666666 => 66.66666666 => 66.67
p3_percent = p3_count / numbers_count * 100 # 0.6666666 => 66.66666666 => 66.67
p4_percent = p4_count / numbers_count * 100 # 0.6666666 => 66.66666666 => 66.67
p5_percent = p5_count / numbers_count * 100 # 0.6666666 => 66.66666666 => 66.67

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")
