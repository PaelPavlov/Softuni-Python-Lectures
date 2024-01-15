# Напишете програма, която изчислява колко време ще ви отнеме да изгледате всички епизоди на един
# сериал в минути. Ще разполагате с брой сезони, брой епизоди на сезон и времетраене на един епизод. Във
# всеки епизод има реклами, които са с продължителност 20% от времето на един епизод. Също така знаете,
# че всеки сезон завършва със специален епизод, който е с 10м по-дълъг от обичайното


series = input()
seasons = int(input())
episodes = int(input())
time = float(input())

bonus_episode = seasons * 10
ads = time * 0.20
episodes_combined = seasons * episodes
time_to_finish = episodes_combined * (time + ads) + bonus_episode

print(f"Total time needed to watch the {series} series is {round(time_to_finish)} minutes.")












# Да се отпечата на конзолата времето, необходимо за изглеждане на всички епизоди, закръглено до най-
# близкото цяло число надолу в следния формат:
# "Total time needed to watch the {име на сериал} series is {време} minutes."