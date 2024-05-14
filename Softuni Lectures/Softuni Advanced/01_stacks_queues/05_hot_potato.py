from collections import deque

kids = deque(input().split())
n = int(input()) - 1
turns = 0

while len(kids) > 1:
    kids.rotate(-n)
#     for i in range(n-1):
#         #get the first kid on the line
#         first_kid = kids.popleft()
#         #move the first kid to the end     
#         kids.append(first_kid)
    print(f"Removed {kids.popleft()}")
print(f"Last is {kids.popleft()}")



