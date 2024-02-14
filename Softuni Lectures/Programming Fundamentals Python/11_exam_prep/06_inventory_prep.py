inventory = input().split(", ")
tasks = []
playing = True

while playing:
    tasks = input().split(" - ")

    if tasks[0] == "Collect":
        new_item = tasks[1]
        if new_item not in inventory:
            inventory.append(new_item)
    elif tasks[0] == "Drop":
        new_item = tasks[1]
        if new_item in inventory:
            inventory.remove(new_item)
        else:
            continue
    elif tasks[0] == "Combine Items":
        old_item, new_item = tasks[1].split(":")
        if old_item in inventory:
            position = inventory.index(old_item)
            inventory.insert(position + 1, new_item)

    elif tasks[0] == "Renew":
        if tasks[1] in inventory:
            inventory.remove(tasks[1])
            inventory.append(tasks[1])
    # elif tasks == "Craft!":
    else:   
        playing = False
        print(", ".join(map(str, inventory)))
        break



