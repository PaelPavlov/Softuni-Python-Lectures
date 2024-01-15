# judge systemata go dava kato greshen, no ne celiqt


budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = 250
cpu_price = gpu_price * gpu_count * 0.35
ram_price = gpu_price * gpu_count * 0.10

sales_total = gpu_count * gpu_price + cpu_price * cpu_count + ram_price * ram_count
sales_discounted = 0

if gpu_count > cpu_count:
    sales_discounted = sales_total * 0.15
    sales_discounted = sales_total - sales_discounted

if sales_discounted != 0 and budget > sales_discounted:
    print(f"You have {budget - sales_discounted:.2f} leva left!")
elif sales_discounted != 0 and budget < sales_discounted:
    print(f"Not enough money! You need {sales_discounted - budget:.2f} leva more!")
elif budget >= sales_total:
    print(f"You have {budget - sales_total:.2f} leva left!")
else:
    print(f"Not enough money! You need {sales_total - budget:.2f} leva more!")
