# year = int(input())
# while True:
#     year += 1
#     is_happy_year = True
#     already_found_digits = ""
#     for digit in str(year):
#         if digit in already_found_digits:
#             is_happy_year = False
#         already_found_digits += digit
#     if is_happy_year:
#         break
# print(year)

year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        break
print(year)