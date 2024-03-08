def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False
 
 
def characters_are_valid(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True
 
 
def no_redundant_symbols(name):
    if " " in name:
        return False
    return True
 
 
def username_is_valid(name):
    if length_is_valid(name) and characters_are_valid(name) and no_redundant_symbols(name):
        return True
    return False
 
 
usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)