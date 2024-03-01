products = {}

while True:
    command = input()

    if command == 'buy':
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {'price': price, 'quantity': quantity}

    else:
        products[name]['quantity'] += quantity

        if products[name]['price'] != price:
            products[name]['price'] = price

for name, info in products.items():
    total_price = info['price'] * info['quantity']
    print(f'{name} -> {total_price:.2f}')
