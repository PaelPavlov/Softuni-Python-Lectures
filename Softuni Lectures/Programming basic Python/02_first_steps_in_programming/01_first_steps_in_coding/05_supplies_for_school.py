# • Пакет химикали - 5.80 лв.

# • Пакет маркери - 7.20 лв.

# • Препарат - 1.20 лв (за литър) 



pens = 5.80
markers = 7.20
cleaning = 1.20

pens_quantity = int(input())
markers_quantity = int(input())
cleaning_quantity = int(input())
namalenie = int(input()) 

namalenie_quantity = namalenie / 100
suma_pens = pens * pens_quantity 
suma_markers = markers * markers_quantity
suma_cleaning = cleaning * cleaning_quantity 
suma_all = suma_cleaning + suma_markers + suma_pens

price_reduction = suma_all * namalenie_quantity

#print("cenata e", suma_all)
#print("spestenata cena", price_reduction)
print("za plashtane", suma_all - price_reduction)
