import re

def valid_destination_function(dest_data):

    pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
    valid_destinations = []
    result = re.finditer(pattern, dest_data)
    travel_points = 0

    for current_destination in result:
        valid_destinations.append(current_destination.group(2))
        travel_points += len(current_destination.group(2))

    print(f'Destinations: {", ".join(valid_destinations)}\n Travel Points: {travel_points}')

data = input()
valid_destination_function(data)