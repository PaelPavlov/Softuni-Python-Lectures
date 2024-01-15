command = input()
student_tickets = 0
standart_tickets = 0
kid_tickets = 0

while command != "Finish":
    movie_name = command
    total_seats = int(input())
    available_seats = total_seats
    ticket_type = input()
    ticket_bought = 0
    while ticket_type != "End":
        ticket_bought += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        elif ticket_type == "standard":
            standart_tickets += 1

        if ticket_bought == total_seats:
            break
        ticket_type = input()

    percent_full = 0
    cinema_full = ticket_bought / total_seats * 100
    print(f"{movie_name} - {cinema_full :.2f}% full.")

    command = input()

total_tickets = standart_tickets + student_tickets + kid_tickets
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100 :.2f}% student tickets.")
print(f"{standart_tickets / total_tickets * 100 :.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100 :.2f}% kids tickets.")
