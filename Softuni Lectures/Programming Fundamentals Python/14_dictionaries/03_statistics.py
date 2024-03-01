statistics = {}
command = input().split(": ")
while command[0] != "statistics":
    product, quantity = command[0], int(command[1])
    if product not in statistics.keys():
        statistics[product] = 0
    statistics[product] += quantity
    command = input().split(": ")
print("Products in stock:")
for product, quantity in statistics.items():
    print(f"- {product}: {quantity}")
count_all_products = len(statistics)
sum_all_quantities =sum(value for value in statistics.values())
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")
 