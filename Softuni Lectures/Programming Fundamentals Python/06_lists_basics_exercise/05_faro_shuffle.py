deck_of_cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2 #Целочислено деление, защото ако ползваме / ще получим 8.0 а не 8
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    deck_after_shuffling = []
    for card_inxed in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_inxed])
        deck_after_shuffling.append(right_part[card_inxed])
    deck_of_cards = deck_after_shuffling

print(deck_of_cards)