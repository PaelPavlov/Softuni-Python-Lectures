from collections import deque

name = input()
queue = deque([])

while name != "End":
    if name == "Paid":
        while queue:
            print(queue.popleft())

    else:
        queue.append()
    
    name = input()