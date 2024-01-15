day_of_the_week = input()
ticket_price = 0

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Friday":
    ticket_price = 12
elif day_of_the_week == "Wednesday" or day_of_the_week == "Thursday":
    ticket_price = 14
elif day_of_the_week == "Sunday" or day_of_the_week == "Saturday":
    ticket_price = 16
print(ticket_price)
