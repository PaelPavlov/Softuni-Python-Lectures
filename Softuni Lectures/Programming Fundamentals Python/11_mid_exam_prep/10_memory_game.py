def main():
    sequence_of_elements = input().split()
    count_moves = 0

    while True:
        count_moves += 1
        command = input()

        if command == "end":
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
            break
        
        index1, index2 = map(int, command.split())

        if is_invalid_input(index1, index2, sequence_of_elements):
            handle_invalid_input(sequence_of_elements, count_moves)
        else:
            handle_valid_input(index1, index2, sequence_of_elements, count_moves)
            



def is_invalid_input(index1, index2, sequence):
    return(
        index1 == index2
        or index1 < 0
        or index2 < 0
        or index1 >= len(sequence)
        or index2 >= len(sequence)
    )

def handle_invalid_input(sequence, count_moves):
    mid_index = len(sequence) // 2
    sequence.insert(mid_index, f'-{count_moves}a')
    sequence.insert(mid_index, f'-{count_moves}a')
    print(f"Invalid input! Adding additional elements to the board")

def handle_valid_input(index1, index2, sequence, count_moves):
    if sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        second_el = sequence[index2]
        sequence.pop(index1)
        sequence.remove(second_el)
    else:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {count_moves} turns!")
        exit()

main()