def palindrome_function(lst):
    result = ''

    for num in lst:
        if str(num) == str(num)[::-1]:
            result += 'True\n'
        else:
            result += 'False\n'
    return result

list_of_palinromes = list(map(int, input().split(', ')))
print(palindrome_function(list_of_palinromes))