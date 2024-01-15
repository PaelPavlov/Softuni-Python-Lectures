
# • Пилешко меню – 10.35 лв.

# • Меню с риба – 12.40 лв.

# • Вегетарианско меню – 8.15 лв. 

CHICKEN_MENU = int(input()) * 10.35
FISH_MENU = int(input()) * 12.40
VEGAN_MENU = int(input()) * 8.15
DELIVERY_PRICE = 2.50

menu_combined = CHICKEN_MENU + VEGAN_MENU + FISH_MENU 

desert_price = menu_combined * 0.20 
total_price = menu_combined + desert_price + DELIVERY_PRICE


print(total_price)
