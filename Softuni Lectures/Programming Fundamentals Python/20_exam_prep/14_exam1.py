followers = {}

while True:
    command = input().split(": ")

    if command[0] == "Log out":
        break

    if command[0] == "New follower":
        username = command[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}

    elif command[0] == "Like":
        username = command[1]
        likes = int(command[2])
        if username not in followers:
            followers[username] = {'likes': likes, 'comments': 0}
        else:
            followers[username]['likes'] += likes
    
    elif command[0] == "Comment":
        username = command[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 1}
        else:
            followers[username]['comments'] += 1

    elif command[0] == "Blocked":
        username = command[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

print(f'{(len(followers))} followers')
for username, info in followers.items():
    print(f"{username}: {info['likes']+info['comments']}")
