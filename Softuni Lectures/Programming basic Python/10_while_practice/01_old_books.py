target_book = input()
books_count = 0
command = input()
while command != "No More Books":
    current_book = command

    if current_book == target_book:
        break
    books_count += 1
    command = input()

if command != "No More Books":
    print(f"The book you search is not here!")
    print(f"You checked {books_count}")
else:
    print(f"You checked {books_count} books and found it.")
