def boarding_passengers(capacity, *groups):
    boarded_passengers = {}
    total_boarded = 0

    for group_size, benefit_program in groups:
        if total_boarded + group_size <= capacity:
            if benefit_program in boarded_passengers:
                boarded_passengers[benefit_program] += group_size
            else:
                boarded_passengers[benefit_program] = group_size
            total_boarded += group_size

    sorted_boarded_passengers = sorted(boarded_passengers.items(), key=lambda x: (-x[1], x[0]))

    result = ["Boarding details by benefit plan:"]
    for benefit_program, count in sorted_boarded_passengers:
        result.append(f"## {benefit_program}: {count} guests")

    if total_boarded == sum(group_size for group_size, _ in groups):
        message = "All passengers are successfully boarded!"
    elif total_boarded == capacity:
        message = "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        available_capacity = capacity - total_boarded
        message = f"Partial boarding completed. Available capacity: {available_capacity}."

    result.append(message)

    return "\n".join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
