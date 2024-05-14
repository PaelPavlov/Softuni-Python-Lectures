from collections import deque


expression = deque(input())
opening_brackets = '([{'
closing_brackets = ')]}'
counter = 0

while expression and counter < len(expression) / 2:
    if expression[0] not in opening_brackets:
        break
    index = opening_brackets.index(expression[0])
    if expression[1] == closing_brackets[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(counter)
        counter = 0
    else:
        expression.rotate(-1)
        counter += 1

if expression:
    print('NO')
else:
    print('YES')