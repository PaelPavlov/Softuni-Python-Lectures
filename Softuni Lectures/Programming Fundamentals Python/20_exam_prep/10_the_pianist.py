def create_composer_data(number_of_pieces):
    composer_dictionary = {}

    for _ in range(number_of_pieces):
        piece, composer, key = input().split("|")
        composer_dictionary[piece] = [composer, key]

    return composer_dictionary

def modifying_data_function(composer_dictionary):

    while True:
        command, *params = input().split("|")
        
        if command == "Stop":
            return composer_dictionary
        
        elif command == "Add":
            piece, composer, key = params[0], params[1], params[2]
            if piece in composer_dictionary:
                print(f"{piece} is already in collection!")
            else:
                composer_dictionary[piece] = [composer, key]
                print(f"{piece} by {composer} in {key} added to the collection!")
        
        elif command == "Remove":
            
            if piece in composer_dictionary:
                del composer_dictionary[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in collection.")

        elif command == "ChangeKey":
            piece, new_key = params[0], params[1]

            if piece in composer_dictionary:
                composer_dictionary[piece][1] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in collection")
            

def base_function(number_of_pieces):
    composer_dictionary = create_composer_data(number_of_pieces)
    modifying_dictionary = modifying_data_function(composer_dictionary)

    for piece, data in modifying_dictionary.items():
        composer, key = data[0], data[1]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


n = int(input())
base_function(n)
