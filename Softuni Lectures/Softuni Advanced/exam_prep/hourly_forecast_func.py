def forecast(*data):
    result = []

    def add_locations(type_of_location):
        locations = []

        for location, weather in data:
            if weather == type_of_location:
                locations.append(location)

        for l in sorted(locations):
            result.append(f"{l} - {type_of_location}")

    add_locations("Sunny")
    add_locations("Cloudy")
    add_locations("Rainy")



    return '\n'.join(result)

