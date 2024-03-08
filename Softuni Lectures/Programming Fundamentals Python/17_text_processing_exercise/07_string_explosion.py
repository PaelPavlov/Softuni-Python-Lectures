some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # Explosion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # > mark
    elif some_string[index] == ">":
        final_string += some_string[index]
        strength += int(some_string[index + 1])
    # No explosion, no > mark
    else:
        final_string += some_string[index]
print(final_string)