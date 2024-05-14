from collections import deque


cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())

wasted_water = 0

while cups and bottles:
    current_cup = cups[0]
    while current_cup > 0:
        current_bottle = bottles.pop()
        current_cup -= current_bottle
    wasted_water -= current_cup
    cups.popleft()

if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
if not bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f'Wasted litters of water: {wasted_water}')