import re
 
 
food_information = input()
pattern= r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
# food = group(2), date = group(3), calories = group(4)
matches = re.findall(pattern,food_information)
total_calories = sum([int(match[3]) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for element in matches:
    item_name = element[1]
    expiration_date = element[2]
    calories = element[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")