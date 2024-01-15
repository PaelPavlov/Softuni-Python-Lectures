# Любо е голям почитател на киното и редовно ходи на прожекции и участва в томболи,
# от които често печели ваучери за кино. Вашата задача е да напишете програма, която да изчислява колко покупки от
# киното може да си купи Любо със спечеленият ваучер. Ако името на покупката съдържа повече от 8 символа, то тя е билет за филм,
# а нейната цена представлява сумата на ASCII символите от първите ѝ два символа. Ако името на покупката съдържа 8 или по-малко символа,
# нейната цена е равна на стойността на първия ASCII символ в името. Любо въвежда името на покупките, които желае, докато не въведе "End"
# или не въведе покупка, чиято стойност е по-голяма от останалата сума на ваучера


# Вход
# Първоначално се чете един ред:
# Стойността на ваучера – цяло число в интервала [1…100000]
# След това до получаване на команда "End" или до изчерпването на ваучера, се чете по един ред:
# Покупката, която Любо е избрал – текст

voucher = int(input())
price = 0
tickets_bought = 0
products_bought = 0
money_left = voucher - price
text = ""
#
# while text != "End":
for _ in range(voucher):
    movie = input()
    if movie == "End":
        break
    elif len(movie) <= 8:
        voucher -= ord(movie[0])
        if voucher < 0:
            break
        products_bought += 1
    elif len(movie) > 8:
        voucher -= (ord(movie[0]) + ord(movie[1]))
        price = ord(movie[0]) + ord(movie[1])
        if voucher < 0:
            break
        tickets_bought += 1

#
# if
print(f"{tickets_bought}")
print(f"{products_bought}")

# Изход
# Програмата приключва при въвеждане на команда "End" или при покупка чиято стойност е по-голяма от останалите пари от ваучера.
# На конзолата трябва да се напечатат три реда:
# "{брои закупени билети}"
# "{брой закупени други покупки}"
