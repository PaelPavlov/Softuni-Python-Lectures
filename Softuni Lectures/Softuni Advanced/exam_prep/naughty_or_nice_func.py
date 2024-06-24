def naughty_or_nice(santa_list, *args, **kwargs):
    nice_kids, naughty_kids = [], []
    result = []

    def place_kid():
        if len(kids) == 1:
            nice_kids.extend(kids) if type_of_kid == "Nice" else naughty_kids.extend(kids)
            santa_list.remove(*kids)

    for kid_data in args:
        number, type_of_kid = kid_data.split("-")
        kids = [info for info in santa_list if info[0] == int(number)]
        place_kid()

    for name, type_of_kid in kwargs.items():
        kids = [info for info in santa_list if info[1] == name]
        place_kid()
        
    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")

    if santa_list:
        result.append(f"Not found: {', '.join(santa_list)}")

    return "\n".join(result)