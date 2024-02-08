def multiplication(num1, num2, num3):
    num_negatives = sum(1 for num in (num1, num2, num3) if num < 0) # Така търсим броят на негативните в нашата функция

    if num_negatives % 2 != 0: # Ако са четен брои, те стават позитивно число. 
        return "negative"
    elif 0 in (num1, num2, num3):
        return "zero"
    else:
        return "positive"
number1, number2, number3, = int(input()), int(input()), int(input())
result = multiplication(number1, number2, number3)

print(result)