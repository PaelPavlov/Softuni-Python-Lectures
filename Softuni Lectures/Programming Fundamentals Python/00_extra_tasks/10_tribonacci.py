def print_tribonacci(number):

    trib_list = [1, 1, 2]
    print("1 1 2", end=" ")
    for i in range(3, number):
        next_num = trib_list[i-3] + trib_list[i-2] + trib_list[i-1]
        trib_list.append(next_num)
        print(next_num, end=" ")

number = int(input())
print_tribonacci(number)

