n = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(n):
    number = int(input())

    if number > 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

count_of_positives = len(positive_numbers)
sum_of_negatives = sum(negative_numbers)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")