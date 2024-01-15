# Задача 3. Филмова премиера
# За предстояща премиера на три известни продукции, местно кино ви наема да напишете софтуер, който да
# изчислява цената, която клиентите трябва да заплатят, според филма и пакета, който са избрали.


movie = input()  #  Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
food = input()  #  Втори ред - пакет за филм - текст с възможности "Drink", "Popcorn" или "Menu"
tickets = int(input())

price = 0
reduction = 0

if movie == "John Wick" and food == "Drink":
    price = 12
elif movie == "John Wick" and food == "Popcorn":
    price = 15
elif movie == "John Wick" and food == "Menu":
    price = 19

if movie == "Star Wars" and food == "Drink":
    price = 18
elif movie == "Star Wars" and food == "Popcorn":
    price = 25
elif movie == "Star Wars" and food == "Menu":
    price = 30

if movie == "Jumanji" and food == "Drink":
    price = 9
elif movie == "Jumanji" and food == "Popcorn":
    price = 11
elif movie == "Jumanji" and food == "Menu":
    price = 14

if movie == "Star Wars" and tickets >= 4:
    reduction = price * 0.30
    price = price - reduction
elif movie == "Jumanji" and tickets == 2:
    reduction = price * 0.15
    price = price - reduction

price_calculation = price * tickets
print(f"Your bill is {price_calculation:.2f} leva.")


# При избран филм "Star Wars" и закупени поне четири билета, има 30% семейна отстъпка.
#  При избран филм "Jumanji" и закупени точно два билета, има 15% отстъпка за двама.
#
# Изход
# На конзолата трябва да се отпечата един ред:
# "Your bill is {крайна цена} leva."
# Цената да бъде закръглена до втората цифра след десетичния знак.
