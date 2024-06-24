#Read athe two sequences # save them in decks
#Define dictionary with key - word and value = word
#while we have sequences, pop from the sequences
#iterate through every word in searched words
# - remove all occurances of the vowel and consonant in the value of the word dict
# - check if we have empty string as value
# - print that a word was found and break loops
#print the rest of the needed output


from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words:
        words[word] = words[word].replace(vowel, '')
        words[word] = words[word].replace(consonant, '')


        if not words[word]:
            print(f"Word found: {word}")
            break
    else:
        continue
    break

else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")