foods_and_quantities = input().split()
final_products = {}
for index in range(0, len(foods_and_quantities), 2):
    product = foods_and_quantities[index]
    quantity = int(foods_and_quantities[index + 1])
    final_products[product] = quantity
print(final_products)