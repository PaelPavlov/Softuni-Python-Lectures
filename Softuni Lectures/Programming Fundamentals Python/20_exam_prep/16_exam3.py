import re
pattern = r"\|([A-Z]+)\|:#([A-Z][a-z]+ [A-Z]?[a-z]+)#"
number_of_bosses = int(input())

for _ in range(number_of_bosses):
    bosses = input()
    matches = re.finditer(pattern, bosses)
    if re.match(pattern, bosses):
        for match in matches:
            print(f"{match[1]}, The {match[2]}")
            print(f">> Strength: {len(match[1])}")
            print(f">> Armor: {len(match[2])}")
    else:
        print(f"Access denied!")


