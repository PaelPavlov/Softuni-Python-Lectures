import sys

movie_count = int(input())
max_rating = -sys.maxsize
min_rating = sys.maxsize
rating_overall = 0
max_movie = ""
min_movie = ""


for x in range(movie_count):
    movie = input()
    rating = float(input())
    rating_overall += rating
    if rating > max_rating:
        max_rating = rating
        max_movie = movie

    if rating < min_rating:
        min_rating = rating
        min_movie = movie

print(f"{max_movie} is with highest rating: {max_rating}")
print(f"{min_movie} is with lowest rating: {min_rating}")
print(f"Average rating:{rating_overall / movie_count:.1f}")



# Изход
# Отпечатват се три реда в следния формат:
# "{име на филма с най-висок рейтинг} is with highest rating: {рейтинг на филма}"
# "{име на филма с най-нисък рейтинг} is with lowest rating: {рейтинг на филма}"
# "Average rating: {средният рейтинг на всички филми}"
