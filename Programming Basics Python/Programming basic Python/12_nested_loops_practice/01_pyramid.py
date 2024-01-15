n = int(input())
counter = 1
is_complete = False
for row in range(1, n + 1):
    for col in range(1, row + 1):

        if counter >= n:
            is_complete = True
            break
        print(str(counter) + ' ', end='')
        counter += 1
    if is_complete:
        break
    print()