def manipulate_distance(distance_list, sum_of_removed_elements, current_index):
    removed_element = 0
    if current_index < 0:
        removed_element = distance_list[0]
        distance_list[0] = distance_list[-1]
    elif current_index >= len(distance_list):
        removed_element = distance_list[-1]
        distance_list[-1] = distance_list[0]
    else:
        removed_element = distance_list.pop(current_index)
    sum_of_removed_elements += removed_element
    for manipulating_index in range(len(distance_list)):
        if distance_list[manipulating_index] <= removed_element:
            distance_list[manipulating_index] += removed_element
        else:
            distance_list[manipulating_index] -= removed_element

    return distance_list, sum_of_removed_elements


distance = [int(number) for number in input().split()]
sum_of_removed_elements = 0

while distance:
    index = int(input())
    distance, sum_of_removed_elements = manipulate_distance(distance, sum_of_removed_elements, index)
print(sum_of_removed_elements)