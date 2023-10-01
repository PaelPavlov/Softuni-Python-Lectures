# · Предпазен найлон - 1.50 лв. за кв. метър

# · Боя - 14.50 лв. за литър

# · Разредител за боя - 5.00 лв. за литър

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
BAG_PRICE = 0.40

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
work_hours_needed = int(input())
nylon_extra_quantity = 2
paint_extra_quantity = paint_quantity * 0.10

total_material_price = (nylon_quantity + nylon_extra_quantity) * NYLON_PRICE + \
    (paint_quantity * paint_extra_quantity) * PAINT_PRICE + \
    PAINT_THINNER_PRICE * paint_thinner_quantity + BAG_PRICE

work_hours_price = total_material_price * 0.30
total_price = total_material_price + work_hours_price * work_hours_needed
print(total_price)