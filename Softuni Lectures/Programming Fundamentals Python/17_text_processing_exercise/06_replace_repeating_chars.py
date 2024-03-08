text = input()
final_text = ""
last_added_character = ""
for current_character in text:
    if current_character != last_added_character:
        final_text += current_character
        last_added_character = current_character
print(final_text)