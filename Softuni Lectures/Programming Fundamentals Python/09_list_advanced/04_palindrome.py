words = input().split()
palindrome_search = input()
palindromes_count = 0
palindromes = []

for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)
        palindromes_count += 1


print(f"{palindromes}")
# print(f"Found palindrome {palindromes_count} times") Търси палиндрома
print(f"Found palindrome {palindromes.count(palindrome_search)} times") # Търси специфична палиндрома, тази която търсим като инпут
