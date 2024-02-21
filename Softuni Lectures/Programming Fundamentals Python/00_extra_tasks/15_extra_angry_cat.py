price_ratings = input().split(", ")
entry_point = int(input())
item_type = input()
left = 0
right = 0

str_to_int = list(map(int, price_ratings))

for idx in range(entry_point - 1, -1, -1):  
    if (item_type == "cheap" and str_to_int[idx] < str_to_int[entry_point]) or \
       (item_type == "expensive" and str_to_int[idx] >= str_to_int[entry_point]):
        left += str_to_int[idx]

for idx in range(entry_point + 1, len(str_to_int)):  
    if (item_type == "cheap" and str_to_int[idx] < str_to_int[entry_point]) or \
       (item_type == "expensive" and str_to_int[idx] >= str_to_int[entry_point]):
        right += str_to_int[idx]


if left >= right:
    print(f"Left - {left}")
else:
    print(f"Right - {right}")
