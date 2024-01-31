# · coffee - 1.50

# · water - 1.00

# · coke - 1.40
product = input()
count = int(input())


def orders(product, count):
    if product == "water":
        return f'{1.00 * count:.2f}'
    elif product == "coffee":
        return f'{1.50* count:.2f}'
    elif product == "coke":
        return f'{1.40 * count:.2f}'
    elif product == "snacks":
        return f'{2.00 * count:.2f}'


result = orders(product, count)
print(result)