price_for_meter = float(7.61)
square_meters = float(input())
discount = float(0.18)

discounted_price = price_for_meter * square_meters * discount
price = price_for_meter * square_meters - discounted_price

print(f"The final price is: {price} lv.")
print(f"The discount is: {discounted_price} lv." )
