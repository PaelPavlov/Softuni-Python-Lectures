animal_type = input()
if animal_type == "dog":
    print("mammal")
elif animal_type == "crocodile" \
        or animal_type == "snake" \
        or animal_type == "tortoise":
    print("reptile")
else:
    print("unknown")
